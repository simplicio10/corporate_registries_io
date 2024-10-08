use std::env;
use std::io;
//use csv::Error;
//use std::fs::File;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    //Control flow based on command line input - refactor into match
    if args[1] == String::from("agent") {
        lookup_agent()?;
    } else {
        println!("Enter a valid search parameter");
    }

    Ok(())
}

//Simple I/O function to return the name of agent
fn lookup_agent() -> io::Result<()> {
    println!("What is the name of the agent?");

    let mut name_agent: String = String::new();

    io::stdin().read_line(&mut name_agent)?;

    println!("The name of the agent is {}", name_agent.trim());
    
    Ok(())
}
