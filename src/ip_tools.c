#include "ip_tools.h"

#include <stdio.h>
#include <stdlib.h>

#include "misc.h"

int main(void) {
    menu();
    return 0;
}

void menu() {
    int menu_choice;
    if (scanf("%d", &menu_choice) == 1) {
        switch (menu_choice) {
            case 1:
                ip_check();
                break;
            case 2:
                mask_check();
                break;
            default:
                achtung();
        }
    } else {
        achtung();
    }
}

void ip_check() {
    IPv4 test_ip;
    input_ipv4(&test_ip);
    output_ip_check(&test_ip);
}

void mask_check() {
    IPv4 test_ip_1, test_ip_2;
    input_ipv4(&test_ip_1);
    input_ipv4(&test_ip_2);
    output_mask_check(&test_ip_1, &test_ip_2);
}