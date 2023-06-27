const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const performCalculation = (num1, operator, num2) => {
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);

    let result;
    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 !== 0) {
                result = num1 / num2;
            } else {
                console.log("Error! Division by zero is not allowed.");
                return;
            }
            break;
        default:
            console.log(`Unknown operator '${operator}'. Please use one of the following: +, -, *, /`);
            return;
    }

    console.log(`The result of ${num1} ${operator} ${num2} is ${result}`);
};

rl.question('Enter the first number: ', (answer1) => {
    rl.question('Enter the operator (+, -, *, /): ', (operator) => {
        rl.question('Enter the second number: ', (answer2) => {
            performCalculation(answer1, operator, answer2);
            rl.close();
        });
    });
});
