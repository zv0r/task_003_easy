#include "ipv4.h"

#include <stdbool.h>
#include <stdint.h>

bool _is_valid_ipv4(int octet_1, int octet_2, int octet_3, int octet_4) {
    return octet_1 >= 0 && octet_1 < 256 && octet_2 >= 0 && octet_2 < 256 && octet_3 >= 0 && octet_3 < 256 &&
           octet_4 >= 0 && octet_4 < 256;
}

uint64_t _calc_ipv4_as_number(int octet_1, int octet_2, int octet_3, int octet_4) {
    return (uint64_t)octet_1 * 1000000000 + octet_2 * 1000000 + octet_3 * 1000 + octet_4;
}

void build_ipv4_address(IPv4 *ip_address, int octet_1, int octet_2, int octet_3, int octet_4) {
    ip_address->octet_1 = octet_1;
    ip_address->octet_2 = octet_2;
    ip_address->octet_3 = octet_3;
    ip_address->octet_4 = octet_4;
    ip_address->as_num = _calc_ipv4_as_number(octet_1, octet_2, octet_3, octet_4);
    ip_address->valid = _is_valid_ipv4(octet_1, octet_2, octet_3, octet_4);
}

bool is_ipv4_from_same_network(const IPv4 *const ip_address_1, const IPv4 *const ip_address_2,
                               unsigned int mask) {
    uint8_t shift = IPV4_BIT_LENGTH - mask;
    return (ip_address_1->as_num >> shift) == (ip_address_2->as_num >> shift);
}