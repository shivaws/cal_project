// calculator.cpp

#include <iostream>

extern "C" {
    int calculate(int num_one, int num_two, int num_three, int choice) {
        int result;
        switch(choice) {
            case 1: // Addition
                result = num_one + num_two;
                break;
            case 2: // Subtraction
                result = num_one - num_two;
                break;
            case 3: // Multiplication
                result = num_one * num_two * num_three;
                break;
            case 4: // Division
                if (num_two == 0) {
                    std::cout << "Please enter a number that is not equal to zero" << std::endl;
                    return -1; // Indicate an error
                }
                result = num_one / num_two;
                break;
            default:
                std::cout << "Please select the correct option from the above list." << std::endl;
                return -1; // Indicate an error
        }
        return result;
    }
}
