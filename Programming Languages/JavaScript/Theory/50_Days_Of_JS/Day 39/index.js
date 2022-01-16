const timeToMixJuice = (name) => {
	// code here
    switch(name)
    {
        case 'Pure Strawberry Joy': return 0.5;
        case 'Energizer':;
        case 'Green Garden': return 1.5;
        case 'Tropical Island': return 3;
        case 'All or Nothing': return 5;
        default: return 2.5;
    }
}

const limesToCut = (wedgesNeeded, limes) => {
	// code here
    let wedges = 0;
    for(let i=0;i<limes.length;i++)
    {
        if(limes[i] === 'small') wedges +=6;
        else if(limes[i] === 'medium') wedges +=8;
        else wedges +=10;

        if(wedges>=wedgesNeeded) return (i+1);
    }
	return limes.length;
}

const remainingOrders = (timeLeft, orders) => {
	// code here
    let timetaken = 0;
    for(let i=0;i<orders.length;i++)
    {
        timetaken += timeToMixJuice(orders[i]);
        orders.splice(0,1);
        if(timetaken>=timeLeft) break;
    }
	return orders;
}
