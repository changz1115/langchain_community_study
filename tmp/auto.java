// validate a phone number 
public boolean validatePhoneNumber(String phoneNumber) {
    // check if phone number is valid
    return phoneNumber.matches("[0-9]{10}");
}

console.log(validatePhoneNumber("321"))

// write a rock,paper,scissors 2 player game 
// import random module 
import java.util.Random; 

// create a list of options 
String[] options = { "rock", "paper", "scissors" }; 


// ask the user to pick rock,paper, or scissors and store it in a variable 
String userChoice = prompt("Enter your choice (rock, paper, or scissors): "); 
