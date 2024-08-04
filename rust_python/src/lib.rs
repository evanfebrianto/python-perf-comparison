use pyo3::prelude::*;

#[pymodule]
fn rust_python(_py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m)]
    fn sum_of_squares_rust(n: u64) -> PyResult<u128> {
        let mut total: u128 = 0;
        for i in 0..n {
            total += (i * i) as u128;
        }
        Ok(total)
    }

    Ok(())
}
