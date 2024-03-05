#ifndef IPV4_H
#define IPV4_H

#include <stdbool.h>
#include <stdint.h>

#define IPV4_BIT_LENGTH 32
#define IPv4_BIT_MASK 24

typedef struct ipv4_t {
    int octet_1;
    int octet_2;
    int octet_3;
    int octet_4;
    uint32_t as_num;
    bool valid;
} IPv4;

void build_ipv4_address(IPv4 *ip_address, int octet_1, int octet_2, int octet_3, int octet_4);

bool is_ipv4_from_same_network(const IPv4 *const ip_address_1, const IPv4 *const ip_address_2,
                               unsigned int mask);

#endif