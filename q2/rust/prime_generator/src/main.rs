use std::env;

fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    } // otherwise we get 2 % 2 == 0!

    for m in 2..n {
        if n % m == 0 {
            return false;
        };
        if m * m > n {
            return true;
        };
    }
    return false;
}

fn generate_primes(primes_to_generate: u32, primestring: &mut String) {

    let mut prime_counter = 0;
    let mut counter = 2;
    while prime_counter < primes_to_generate {
        if is_prime(counter) {
            prime_counter = prime_counter + 1;
            let spr = counter.to_string();
            primestring.push_str(&spr);
        }
        counter = counter + 1;
    }   
}

fn get_primes_from_position(pos: usize, primes: &mut String) {
        
    if pos > 10000 {
        return;
    }
    // Generate all primes from 0 to 10000
    let mut primestring = String::new();
    generate_primes(10005, &mut primestring);
    
    // Copying sliced part individually
    let pos_final = pos + 5;
    for i in pos..pos_final {
        let data = &primestring[i..i+1].to_string();
        primes.push_str(data);
    }
}

fn main() {
    // Argument reading
    let args: Vec<String> = env::args().collect();
    let position = &args[1];
    let pos = position.parse::<usize>().unwrap();
    // Search for the required string  
    let mut primestring = String::new();
    get_primes_from_position(pos,  &mut primestring);
    println!("{}", primestring);  
}