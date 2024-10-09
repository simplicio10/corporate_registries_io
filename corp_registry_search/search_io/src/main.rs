use std::env;
use std::io;

use search_io::match_input;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    match_input(&args)
}


