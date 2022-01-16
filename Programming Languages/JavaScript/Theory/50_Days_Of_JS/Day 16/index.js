const isUpper = (string) => {
    return !/[a-z]/.test(string) && /[A-Z]/.test(string)
}

function hey(message) {
	// Code here
    let pureLetterString = ""
    message.split("").forEach(character => {
        if(/[a-zA-Z]/.test(character)){
            pureLetterString += character
        }
    })

    if(isUpper(pureLetterString) && message.trim().charAt(message.length-1) === '?'){
        return "Calm down, I know what I'm doing!"
    }
    else if(isUpper(pureLetterString)){
        return "Whoa, chill out!"
    }
    else if(message.trim().charAt(message.length-1) === '?'){
        return "Sure."
    }
    else if(message === ""){
        return "Fine. Be that way!"
    }

	return "Whatever."
}
