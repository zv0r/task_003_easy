#include "mask_check.h"

#include <stdio.h>

#include "ipv4.h"
#include "misc.h"

int main(void) {
    IPv4 test_ip_1, test_ip_2;
    input_ipv4(&test_ip_1);
    input_ipv4(&test_ip_2);
    output(&test_ip_1, &test_ip_2);
    return 0;
}

void output(const IPv4 *const ip_address_1, const IPv4 *const ip_address_2) {
    printf(is_ipv4_from_same_network(ip_address_1, ip_address_2, IPV4_BIT_MASK) ? "YES" : "NO");
}