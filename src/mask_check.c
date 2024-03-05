#include <stdio.h>

#include "ipv4.h"
#include "misc.h"

int main(void) {
    IPv4 test_ip_1, test_ip_2;
    input_ipv4(&test_ip_1);
    input_ipv4(&test_ip_2);
    output_mask_check(&test_ip_1, &test_ip_2);
    return 0;
}
