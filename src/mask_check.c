#include "mask_check.h"

#include <stdio.h>

#include "ipv4.h"

int main(void) {
    IPv4 test_ip_1, test_ip_2;
    input(&test_ip_1);
    input(&test_ip_2);
    output(&test_ip_1, &test_ip_2);
    return 0;
}

void input(IPv4 *ip_address) {
    int octet_1, octet_2, octet_3, octet_4;

    scanf("%d.%d.%d.%d", &octet_1, &octet_2, &octet_3, &octet_4);
    build_ipv4_address(ip_address, octet_1, octet_2, octet_3, octet_4);
}

void output(const IPv4 *const ip_address_1, const IPv4 *const ip_address_2) {
    printf(is_ipv4_from_same_network(ip_address_1, ip_address_2, IPV4_BIT_MASK) ? "YES" : "NO");
}