use std::io;

//Control flow based on command line input
pub fn match_input(args: &[String]) -> io::Result<()> {
    match args.get(1).map(String::as_str) {
        Some("agent") => lookup_agent(),
        Some(_) => {
            println!("Enter a valid search parameter");
            Ok(())
        },
        None => {
            println!("No argument entered");
            Ok(())}
    }
}

//Simple I/O function to return the name of agent -- add case matching
fn lookup_agent() -> io::Result<()> {
    println!("What is the name of the agent?");

    let mut name_agent: String = String::new();

    io::stdin().read_line(&mut name_agent)?;

    //Refactor into Postgres search
    println!("The name of the agent is {}", name_agent.trim());

    Ok(())
}