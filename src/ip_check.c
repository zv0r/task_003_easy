#include "ip_check.h"

#include <stdio.h>

#include "ipv4.h"
#include "misc.h"

int main(void) {
    IPv4 test_ip;
    input_ipv4(&test_ip);
    output(&test_ip);
    return 0;
}

void output(const IPv4 *const ip_address) { printf(ip_address->valid ? "VALID" : "INVALID"); }