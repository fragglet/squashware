// Command line program to push to BIOS keyboard buffer.
// A (better) reimplementation of STUFFBUF that shipped with EDMAP.
#include <i86.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <process.h>

static char cmdbuf[129];

static const int scantochar[128] = {
	0, 27, '1', '2', '3', '4', '5', '6',
	'7', '8', '9', '0', '-', '=', '\b' /* backspace */, 9 /* tab */,
	'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
	'o', 'p', '[', ']', 13 /* enter */, 0, 'a', 's',
	'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
	'\'', '`', 0, '\\', 'z', 'x', 'c', 'v',
	'b', 'n', 'm', ',', '.', '/', 0, 0,
	0, ' ',
};

static int chartoscan[128];

void make_chartoscan(void)
{
    int i;
    for (i = 0; i < 128; i++)
    {
        if (scantochar[i] > 0)
        {
            chartoscan[scantochar[i]] = i;
        }
    }
    chartoscan['\n'] = chartoscan['\r'];
}

void simulate_keypress(int c)
{
    union REGS r;

    r.h.ah = 0x05; // store keystroke
    r.h.cl = c;
    r.h.ch = chartoscan[c];
    int86(0x16, &r, &r);
}

int unescape(int c)
{
    switch (c)
    {
    case 'e':
        return 27;
    case 'n':
        return '\n';
    case 'r':
        return '\r';
    case 't':
        return '\t';
    case '\\':
        return '\\';
    case 'b':
        return '\b';
    default:
        return 0;
    }
}

int main(int argc, char *argv[])
{
    int i, c, e;

    // We get the raw command line provided by DOS, so that eg.
    // spaces can be supplied to the program.
    getcmd(cmdbuf);

    if (strlen(cmdbuf) == 0)
    {
        printf("Usage: %s [string]\n", argv[0]);
        exit(1);
    }

    make_chartoscan();

    for (i = 0; cmdbuf[i] != '\0'; i++)
    {
        c = cmdbuf[i];
        if (c == '\\')
        {
            int e = unescape(cmdbuf[i + 1]);
            if (e == 0)
            {
                printf("Unknown escape '\\%c'\n", cmdbuf[i + 1]);
                exit(-1);
            }
            simulate_keypress(e);
            i++;
        }
        else
        {
            simulate_keypress(c);
        }
    }

    return 0;
}
