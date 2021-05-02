use std::env;
mod primes;

fn main() {
    // Argument reading
    let args: Vec<String> = env::args().collect();
    let position = &args[1];
    let pos = position.parse::<usize>().unwrap();
    // Search for the required string  
    let mut primestring = String::new();
    primes::get_primes_from_position(pos,  &mut primestring);
    println!("{}", primestring);  
}