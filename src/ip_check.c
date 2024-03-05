#include <stdio.h>

#include "ipv4.h"
#include "misc.h"

int main(void) {
    IPv4 test_ip;
    input_ipv4(&test_ip);
    output_ip_check(&test_ip);
    return 0;
}
