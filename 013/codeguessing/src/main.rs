#[allow(all)]
use std::io::Read;
/// I don't have any good ideas for this
/// round of code-guessing so I'm going
/// to send a regular rust code

#[derive(Debug, Clone, Copy, Default, PartialEq, PartialOrd, Eq)]
struct Rules<'pattern> {
    from: &'pattern str,
    to: &'pattern str,
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args[1] == "-c" {
        let infile = args[2].clone();
        let outfile = args[3].clone();

        let mut bf = unsafe {String::from_utf8_unchecked(std::fs::read(infile).unwrap())};
        let rules = [
            Rules { from: "+-", to: "" },
            Rules { from: "-+", to: "" },
            Rules { from: "<>", to: "" },
            Rules { from: "><", to: "" },
            Rules { from: "+[-]", to: "[-]" },
            Rules { from: "-[-]", to: "[-]" },
            Rules { from: "+[+]", to: "[+]" },
            Rules { from: "-[+]", to: "[+]" },
            Rules { from: "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", to: "" },
            Rules { from: "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", to: "" },
        ];
        for _ in 0..10 {
            for rule in rules {
                while true {
                    let new = bf.replace(rule.from, rule.to);
                    if new == bf {
                        break;
                    }
                    bf = new;
                }
            }
        }

        std::fs::write(outfile, bf.as_bytes()).unwrap();
    }
    else {
        let file = args[2].clone();
        let bf = std::fs::read(file).unwrap();

        let mut tape = vec![0; 30000];
        let mut pointer = 0;
        let mut pointer2 = 0;
        while true {
            if pointer >= bf.len() {
                std::process::exit(0);
            }
            if bf[pointer] == b'+' {
                tape[pointer2] = tape[pointer2] + 1;
            }
            if bf[pointer] == b'-' {
                tape[pointer2] = tape[pointer2] - 1;
            }
            if bf[pointer] == b'>' {
                pointer2 = pointer2 + 1;
            }
            if bf[pointer] == b'<' {
                pointer2 = pointer2 - 1;
            }
            if bf[pointer] == b'.' {
                print!("{}", char::from(tape[pointer2]));
            }
            if bf[pointer] == b',' {
                let mut buf = Vec::new();
                buf.push(0);
                std::io::stdin().read_exact(&mut buf).unwrap();
                tape[pointer2] = *buf.first().unwrap();
            }
            if bf[pointer] == b'[' {
                if tape[pointer2] == 0 {
                    let mut i = pointer + 1;
                    let mut j = 1;
                    while true {
                        if bf[i] == b']' {
                            j = j - 1
                        }
                        if bf[i] == b'[' {
                            j = j + 1
                        }
                        if j == 0 {
                            break;
                        }
                        i = i + 1;
                    }
                    pointer = i;
                }
            }
            if bf[pointer] == b']' {
                if tape[pointer2] != 0 {
                    let mut i = pointer - 1;
                    let mut j = 1;
                    while true {
                        if bf[i] == b'[' {
                            j = j - 1
                        }
                        if bf[i] == b']' {
                            j = j + 1
                        }
                        if j == 0 {
                            break;
                        }
                        i = i - 1;
                    }
                    pointer = i;
                }
            }
            pointer = pointer + 1;
        }

    }
}
