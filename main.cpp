#define _USE_MATH_DEFINES
#define EPS 1e-10

#include <iostream>
#include <cmath>
#include <chrono>

typedef std::chrono::high_resolution_clock Clock;

int main() {
	const long double a = 1;
	long double lhs = 0;
	long double rhs =
		(M_PI / 4 * powl (a, 2))
		* ((coshl(M_PI * M_SQRT2 * a) + cosl(M_PI * M_SQRT2 * a)) 
			/ (coshl(M_PI * M_SQRT2 * a) - cosl(M_PI * M_SQRT2 * a)))
		- (1 / (4 * M_PI * pow(a, 4)));
	long double diff = 0;

	int k = 0;
	auto t1 = Clock::now();

	for (k = 1; k != 100000000; ++k) {
		lhs += (k / (powl(k, 4) + powl(a, 4))) * (1 / tanhl(k * M_PI));
		diff = abs(lhs - rhs);

		if (EPS > diff) {
			auto t2 = Clock::now();
			std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);

			std::cout << "> Time passed: " << time_span.count() << " seconds" << std::endl;
			std::cout.precision(10);
			std::cout << "> Series stopped at " << k << std::endl
				<< "> Left hand side argument is " << lhs << std::endl
				<< "> Right hand side argument is " << rhs << std::endl
				<< "> Absolute difference is " << diff << std::endl;
			return 0;
		}
	}
	std::cout << "Loop stopped at " << k << "-iteration.." << std::endl;
	return 1;
}