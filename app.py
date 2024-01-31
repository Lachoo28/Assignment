import streamlit as st

st.title('Assignment')

st.header("Question 01")
st.subheader("VehicleBill.js")

code = '''import java.util.Scanner;

public class VehicleBill {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input customer details
        System.out.print("Enter the Customer NIC Number: ");
        String nicNumber = scanner.nextLine();

        System.out.print("Enter the Customer Name: ");
        String customerName = scanner.nextLine();

        System.out.print("Enter the Customer Address: ");
        String customerAddress = scanner.nextLine();

        System.out.print("Enter the Phone Number: ");
        String phoneNumber = scanner.nextLine();

        System.out.print("Enter the Vehicle Type: ");
        String vehicleType = scanner.nextLine();

        System.out.print("Enter the Travelled Distance (in Km): ");
        double travelledDistance = scanner.nextDouble();

        // Calculate total charge bill
        double totalCharge = calculateTotalCharge(vehicleType, travelledDistance);
        double discount = calculateDiscount(totalCharge);
        double totalChargeToPay = totalCharge - discount;

        // Output the result
        System.out.println("\n***Total Charge Bill***");
        System.out.println("NIC Number: " + nicNumber);
        System.out.println("Customer Name: " + customerName);
        System.out.println("Customer Address: " + customerAddress);
        System.out.println("Phone Number: " + phoneNumber);
        System.out.println("Vehicle Type: " + vehicleType);
        System.out.println("Travelled Distance: " + travelledDistance + " Km");
        System.out.println("Total Charge: Rs. " + totalCharge);
        System.out.println("Discount: Rs. " + discount);
        System.out.println("Total Charge to Pay: Rs. " + totalChargeToPay);

        // Close the scanner
        scanner.close();
    }

    private static double calculateTotalCharge(String vehicleType, double travelledDistance) {
        if (vehicleType.equalsIgnoreCase("Toyota Corolla")) {
            if (travelledDistance < 50) {
                return travelledDistance * 50;
            } else if (travelledDistance < 200) {
                return 50 * 50 + (travelledDistance - 50) * 100;
            } else {
                return 50 * 50 + 150 * 100 + (travelledDistance - 200) * 150;
            }
        } else {
            if (travelledDistance < 50) {
                return travelledDistance * 75;
            } else if (travelledDistance < 200) {
                return 50 * 50 + (travelledDistance - 50) * 125;
            } else {
                return 50 * 50 + 150 * 100 + (travelledDistance - 200) * 175;
            }
        }
    }

    private static double calculateDiscount(double totalCharge) {
        if (totalCharge > 15000) {
            // 2% discount for total charge > 15000
            return totalCharge * 0.02;
        } else if (totalCharge > 5000) {
            // 0.05% discount for 5000 < total charge <= 15000
            return totalCharge * 0.0005;
        } else {
            return 0;
        }
    }
}'''
st.code(code, language='java')

st.divider()
st.header("Question 02")
st.subheader("Summation.js")

code = '''public class Summation {
    public static void main(String[] args) {
        int firstNumber = 1;
        int secondNumber = 1;
        int sum = 2; 

        System.out.println("Sum of the first 50 numbers in the series:");

        for (int i = 3; i <= 50; i++) {
            
            int nextNumber = firstNumber + secondNumber;

            
            sum += nextNumber;

            
            firstNumber = secondNumber;
            secondNumber = nextNumber;
        }

        
        System.out.println(sum);
    }
}
'''
st.code(code, language='java')

st.divider()
st.header("Question 03")
st.subheader("Average.js | do while loop")

code = '''public class Average {
    public static void main(String[] args) {
        int sum = 0;
        int count = 0;
        int number = 1;

        System.out.println("Odd numbers in multiples of 9 from 1 to 100:");

        do {
            if (number % 2 != 0 && number % 9 == 0) {
                System.out.print(number);

                // Add the number to the sum
                sum += number;

                // Increment the count of numbers
                count++;

                // Print a comma and space unless it's the last number
                if (number < 99) {
                    System.out.print(", ");
                }
            }

            // Move to the next number
            number++;
        } while (number <= 100);

        // Calculate and print the average
        if (count > 0) {
            double average = (double) sum / count;
            System.out.println("\nAverage of the numbers: " + average);
        } else {
            System.out.println("\nNo odd numbers in multiples of 9 found.");
        }
    }
}
'''
st.code(code, language='java')

st.divider()
st.header("Question 04")
st.subheader("Average.js | while loop")

code = '''public class Average {
    public static void main(String[] args) {
        int sum = 0;
        int count = 0;
        int number = 2; 

        System.out.println("Prime numbers in integers from 1 to 100:");

        while (number <= 100) {
            if (isPrime(number)) {
                System.out.print(number);

                
                sum += number;

                
                count++;

                
                if (number < 100) {
                    System.out.print(", ");
                }
            }

            
            number++;
        }

        
        if (count > 0) {
            double average = (double) sum / count;
            System.out.println("\nAverage of the prime numbers: " + average);
        } else {
            System.out.println("\nNo prime numbers found in the range.");
        }
    }

    
    private static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
'''
st.code(code, language='java')

st.divider()
st.header("Question 05")
st.subheader("Pattern.js | while loop")

code = '''public class pattern {
    public static void main(String[] args) {
        int row = 1;

        System.out.println("Pattern:");

        while (row <= 5) {
            int column = 1;

            while (column <= row) {
                System.out.print("*");
                column++;
            }

            System.out.println();
            row++;
        }
    }
}

'''
st.code(code, language='java')

st.divider()
st.header("Question 06")
st.subheader("Pattern.js | for  loop")

code = '''public class pattern {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            if (i % 2 == 1) {
                
                for (int j = 1; j <= 5; j++) {
                    System.out.print("*");
                }
            } else {
                
                System.out.print(" ");
                for (int j = 1; j <= 3; j++) {
                    System.out.print("*");
                }
            }
            System.out.println();  
        }
    }
}
'''
st.code(code, language='java')
