use std::env;


fn my_first_function(args :Vec<String> ) -> Result<(), std::io::Error> {

    println!("{:?}", args);
    std::process::exit(84)
}

fn main() -> Result<(), std::io::Error> {
    let args: Vec<String> = env::args().collect();

    return my_first_function(args);
}
