#include "misc.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

void achtung() {
    fprintf(stderr, "Puck you, Verter!");
    exit(EXIT_FAILURE);
}

int _octets_count(const char* ip_address_str) {
    int result = 1;
    for (int i = 0; ip_address_str[i] != 0; i++) {
        if (ip_address_str[i] == '.') result++;
    }
    return result;
}

int _ipv4_doesnt_contains_letters(const char* const ip_address_str) {
    int letters = 0;
    for (int i = 0; ip_address_str[i] != 0; i++) {
        if ((ip_address_str[i] < '0' || ip_address_str[i] > '9') && ip_address_str[i] != '.') {
            letters++;
        }
    }
    return !letters;
}

int _set_octet_value(const char* number_str, int* number_ptr) {
    *number_ptr = (int)strtol(number_str, NULL, 10);
    return number_str[0] == '0' && strlen(number_str) > 1;
}

int _parse_octets(char* ip_address_str, int* octet_1, int* octet_2, int* octet_3, int* octet_4) {
    int result = 1;
    if (_octets_count(ip_address_str) == 4 && _ipv4_doesnt_contains_letters(ip_address_str)) {
        result += _set_octet_value(strtok(ip_address_str, "."), octet_1);
        result += _set_octet_value(strtok(NULL, "."), octet_2);
        result += _set_octet_value(strtok(NULL, "."), octet_3);
        result += _set_octet_value(strtok(NULL, "."), octet_4);
    } else {
        result = 0;
    }
    return result;
}

void input_ipv4(IPv4* ip_address) {
    char* ip_address_str = NULL;
    int octet_1, octet_2, octet_3, octet_4, parse_octets_result;
    if (scanf("%ms", &ip_address_str) == 1 &&
        (parse_octets_result = _parse_octets(ip_address_str, &octet_1, &octet_2, &octet_3, &octet_4))) {
        build_ipv4_address(ip_address, octet_1, octet_2, octet_3, octet_4);
        if (parse_octets_result > 1) {
            ip_address->valid = false;
        }
        free(ip_address_str);
    } else {
        free(ip_address_str);
        achtung();
    }
}

void output_ip_check(const IPv4* const ip_address) { printf(ip_address->valid ? "VALID" : "INVALID"); }

void output_mask_check(const IPv4* const ip_address_1, const IPv4* const ip_address_2) {
    printf(is_ipv4_from_same_network(ip_address_1, ip_address_2, IPV4_BIT_MASK) ? "YES" : "NO");
}