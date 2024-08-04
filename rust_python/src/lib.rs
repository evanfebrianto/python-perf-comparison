use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn rust_python(_py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m)]
    fn sum_of_squares_rust(n: usize) -> PyResult<u128> {  // Changed usize to u128
        let mut total: u128 = 0;  // Changed total type to u128
        for i in 0..n as u128 {  // Cast loop variable to u128
            total = total.checked_add(i * i).ok_or_else(|| {
                PyErr::new::<pyo3::exceptions::PyOverflowError, _>("Overflow occurred")
            })?;
        }
        Ok(total)
    }

    Ok(())
}
