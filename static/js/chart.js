const makeGoal = (baseline, colour) => {
	if(isNaN(baseline) || baseline === "") {
		throw new TypeError("baseline is not a number");
	}
	if(baseline < 0 || baseline > 100) {
		throw new RangeError("baseline is outside acceptable range of values")
	}
	return {
		name: "Baseline",
		value: baseline,
		strokeWidth: 5,
		strokeHeight: 10,
		strokeColor: colour
	};
}

const mapScores = (functions, scores, baselines) => {
	func = functions[0];
	score = scores[0];
	baseline = baselines[0];

	return {
				x: func,
				y: score,
				goals: [{
					name: "Baseline",
					value: baseline,
					strokeWidth: 5,
					strokeHeight: 10,
					strokeColor: "#7EB2DD"
				}]
		};
}

const mapFunctionScores = (functions, scores, baselines, functionColours) => {
	let functionScores = [];

	for(let i = 0; i < functions.length; i++) {
		let score = {
				x: functions[i],
				y: scores[i],
				goals: [makeGoal(baselines[i], functionColours["baseline"])]
		};
		functionScores.push(score);
	}

	return functionScores;
}

const combineScores = (functions, scores, baselines) => {
	let combined = [];

	let combinedScores = {}
	for(let i = 0; i < functions.length; i++) {
		combinedScores = {
			"function": functions[i],
			"score": scores[i],
			"baseline": baselines[i]
		};

		combined.push(combinedScores);
	}

	return combined;
}

const createOptions = (functions, scores, baselines, functionColours) => {
	let functionScores = mapFunctionScores(functions, scores, baselines, functionColours);
	let optionsObject = {
		        series: [{
		          	name: "Latest",
		          	data: functionScores
		          }],
		          chart: {
		          type: "bar",
		          height: 380
		        },
		        plotOptions: {
		          bar: {
		            distributed: true,
		            horizontal: true,
		            dataLabels: { position: "bottom" },
		          }
		        },
		        colors: [functionColours["bar"]],
		        dataLabels: {
		          enabled: true,
		          textAnchor: "start",
		          style: {
		            colors: [functionColours["label"]]
		          },
		          formatter: function (val, opt) {
		            return opt.w.globals.labels[opt.dataPointIndex]
		          },
		          offsetX: 0,
		          dropShadow: { enabled: false }
		        },
		        stroke: {
		          width: 1,
		          colors: ["#fff"]
		        },
		        xaxis: { categories: functions },
		        yaxis: {
		          labels: {
		            show: false
		          }
		        },
		        title: {
		            text: "Function Skill Scores",
		            align: "center",
		            floating: true
		        },
		        subtitle: {
		            text: "Percentage of total score available for the function",
		            align: "center",
		        },
		        tooltip: {
		          theme: "dark",
		          x: { show: false },
		          y: {
			            formatter: function (val, opt) {
			                return val + "%";
			            }
		          }
		        },
		        legend: {
		          show: true,
		          showForSingleSeries: true,
		          customLegendItems: ["Latest", "Baseline"],
		          markers: {
		            fillColors: [functionColours["bar"], functionColours["baseline"]]
		          }
		        }

		    };

		    return optionsObject;
}

/* To export more than one item we need to place them in curly braces */
module.exports = { makeGoal, mapScores, combineScores, mapFunctionScores, createOptions };