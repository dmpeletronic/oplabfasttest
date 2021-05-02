/// Check if a number is prime.
/// Return true when the number is prime, false otherwise
///
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

/// Generate a big string with N prime numbers concatenated accordingly
/// to parameter primes_to_generate.
///
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

/// Generates a string taking the position p from parameter and 
/// the list of all 100000 prime numbers.
/// 
/// The resultant string will be 5 chars long.
///
pub fn get_primes_from_position(pos: usize, primes: &mut String) {
        
    if pos > 10000 {
        return;
    }    
    // Generate all primes from 0 to 10000
    let mut primestring = String::new();
    generate_primes(10005, &mut primestring);
    
    // Copying sliced part individually
    primes.clear();
    let pos_final = pos + 5;
    for i in pos..pos_final {
        let data = &primestring[i..i+1].to_string();
        primes.push_str(data);
    }
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_prime() {
        assert_eq!(is_prime(0), false);
        assert_eq!(is_prime(1), false);
        assert!(is_prime(2));
        assert!(is_prime(5));
        assert!(is_prime(7));
        assert!(!is_prime(9));
        assert!(is_prime(13));
        assert!(!is_prime(45));
        assert!(!is_prime(13 * 13));    
        assert!(is_prime(7919));
        assert!(is_prime(23509));
        assert!(is_prime(29483));
        assert!(is_prime(48821));
        assert!(is_prime(55673));
        assert!(is_prime(68699));
        assert!(!is_prime(1000000));
        assert!(!is_prime(2000001));

    }

    #[test]
    fn test_generage_primes() {
        let mut primestring = String::new();
        generate_primes(5, &mut primestring);
        assert_eq!(&primestring, "235711");

        primestring.clear();
        generate_primes(0, &mut primestring);
        assert_eq!(&primestring, "");

        primestring.clear();
        generate_primes(10, &mut primestring);
        assert_eq!(&primestring, "2357111317192329");
    }

    #[test]
    fn test_pos() {
        let mut primestring = String::new();
        get_primes_from_position(0,  &mut primestring);
        assert_eq!(&primestring, "23571");

        primestring.clear();
        get_primes_from_position(3,  &mut primestring);
        assert_eq!(&primestring, "71113");

        primestring.clear();
        get_primes_from_position(5,  &mut primestring);
        assert_eq!(&primestring, "11317");
    }
}