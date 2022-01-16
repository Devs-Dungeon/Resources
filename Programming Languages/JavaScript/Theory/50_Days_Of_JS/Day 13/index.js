const spaceAge = (seconds) => {
	const yearsInAllPlanets = {
		Mercury: 0,
		Venus: 0,
		Earth: 0,
		Mars: 0,
		Jupiter: 0,
		Saturn: 0,
		Uranus: 0,
		Neptune: 0,
	}

	// Your solution starts here

    yearsInAllPlanets.Mercury = parseFloat((parseFloat(seconds) / (31557600 * 0.2408467)).toFixed(2))
    yearsInAllPlanets.Venus = parseFloat((parseFloat(seconds) / (31557600 * 0.61519726)).toFixed(2))
    yearsInAllPlanets.Earth = parseFloat((parseFloat(seconds) / (31557600)).toFixed(2))
    yearsInAllPlanets.Mars = parseFloat((parseFloat(seconds) / (31557600 * 1.8808158)).toFixed(2))
    yearsInAllPlanets.Jupiter = parseFloat((parseFloat(seconds) / (31557600 * 11.862615)).toFixed(2))
    yearsInAllPlanets.Saturn = parseFloat((parseFloat(seconds) / (31557600 * 29.447498)).toFixed(2))
    yearsInAllPlanets.Uranus = parseFloat((parseFloat(seconds) / (31557600 * 84.016846)).toFixed(2))
    yearsInAllPlanets.Neptune = parseFloat((parseFloat(seconds) / (31557600 * 164.79132)).toFixed(2))

	// Your solution ends here

	return yearsInAllPlanets
}

console.log(spaceAge(Math.round(Math.random() * 99999999)))
