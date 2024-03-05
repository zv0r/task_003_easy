all: build

build: ip_tools mask_check ip_check

ip_check: src/ip_check.c src/ipv4.c
	gcc -Wall -Werror -Wextra -std=c11 -o ./src/ip_check ./src/ip_check.c ./src/ipv4.c ./src/misc.c

mask_check: src/mask_check.c src/ipv4.c
	gcc -Wall -Werror -Wextra -std=c11 -o ./src/mask_check ./src/mask_check.c ./src/ipv4.c ./src/misc.c

ip_tools: src/ip_tools.c src/ipv4.c
	gcc -Wall -Werror -Wextra -std=c11 -o ./bin/ip_tools ./src/ip_tools.c ./src/ipv4.c ./src/misc.c
