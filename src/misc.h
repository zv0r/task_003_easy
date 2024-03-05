#ifndef MISC_H
#define MISC_H

#include "ipv4.h"

void achtung();

void input_ipv4(IPv4 *ip_address);

void output_ip_check(const IPv4 *const ip_address);

void output_mask_check(const IPv4 *const ip_address_1, const IPv4 *const ip_address_2);

#endif