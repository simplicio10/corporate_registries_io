use std::io;
use postgres::{Client, NoTls, Error};

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

    //Case matching here
    let mut name_agent: String = String::new();

    io::stdin().read_line(&mut name_agent)?;

    //Refactor into Postgres search
    let mut client = Client::connect("host=localhost user=postgres password=password dbname=corp_registry_test", NoTls)?;

    for row in client.query("SELECT * FROM llc_agent_il WHERE agent_name= $1", &[&name_agent])? {
        let result: i32 = row.get("*");
        println!("agent_info: {}", result);
    }

    Ok(())
}