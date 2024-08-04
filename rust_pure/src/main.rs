use std::time::Instant;

fn sum_of_squares(n: u128) -> u128 {
    let mut total: u128 = 0;
    for i in 0..n {
        total += i * i;
    }
    total
}

fn main() {
    let n: u128 = 10_000_000; // Define the range
    
    let start = Instant::now();
    let result = sum_of_squares(n);
    let duration = start.elapsed();

    println!("Result: {}", result);
    println!("Execution Time (Pure Rust): {:?}", duration);
}
