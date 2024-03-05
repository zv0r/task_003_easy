#include "ip_check.h"

#include <stdio.h>

#include "ipv4.h"

int main(void) {
    int octet_1, octet_2, octet_3, octet_4;
    IPv4 test_ip;
    scanf("%d.%d.%d.%d", &octet_1, &octet_2, &octet_3, &octet_4);
    build_ipv4_address(&test_ip, octet_1, octet_2, octet_3, octet_4);
    output(&test_ip);
    return 0;
}

void output(const IPv4 *const ip_address) { printf(ip_address->valid ? "VALID" : "INVALID"); }