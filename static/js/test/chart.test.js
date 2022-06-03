/*Import the function that we are testing from the chart.js file*/
let {makeGoal, mapScores, combineScores, mapFunctionScores, createOptions} = require("../chart.js");

/*Add test code*/
/*'describe' signifies a test / test suite
Top level parent 'describe', i.e. Test Suite*/
describe("Chart", () => {
	/*Child test suite*/
	describe("Make single goal", () => {
		test("makeGoal() should return a goal", () => {
			expectedGoal = {
				name: 'Baseline',
				value: 70,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: '#7EB2DD'
			};

			actualGoal = makeGoal(70, "#7EB2DD");

			expect(expectedGoal).toEqual(actualGoal);
		});
		test("makeGoal() should return a goal with a different score", () => {
			expectedGoal = {
				name: 'Baseline',
				value: 50,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: '#7EB2DD'
			};

			actualGoal = makeGoal(50, "#7EB2DD");

			expect(expectedGoal).toEqual(actualGoal);
		});
		test("makeGoal() should return a goal with a score of 100", () => {
			expectedGoal = {
				name: 'Baseline',
				value: 100,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: '#7EB2DD'
			};

			actualGoal = makeGoal(100, "#7EB2DD");

			expect(expectedGoal).toEqual(actualGoal);
		});
		test("makeGoal() should return a goal with a score of 0", () => {
			expectedGoal = {
				name: 'Baseline',
				value: 0,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: '#7EB2DD'
			};

			actualGoal = makeGoal(0, "#7EB2DD");

			expect(expectedGoal).toEqual(actualGoal);
		});
		test("makeGoal() should throw a TypeError if a String is entered", () => {
			/*https://stackoverflow.com/questions/46042613/how-to-test-the-type-of-a-thrown-exception-in-jest*/
			expect.assertions(2)
			try {
				actualGoal = makeGoal("seventy", "#7EB2DD");
			} catch(ex) {
				expect(ex.message).toBe("baseline is not a number");
				expect(ex.name).toBe("TypeError");
			}
		});
		test("makeGoal() should throw a TypeError if an empty String is entered", () => {
			/*https://stackoverflow.com/questions/46042613/how-to-test-the-type-of-a-thrown-exception-in-jest*/
			expect.assertions(2)
			try {
				actualGoal = makeGoal("", "#7EB2DD");
			} catch(ex) {
				expect(ex.message).toBe("baseline is not a number");
				expect(ex.name).toBe("TypeError");
			}
		});
		test("makeGoal() should throw a RangeError if a negative number is entered", () => {
			/*https://stackoverflow.com/questions/46042613/how-to-test-the-type-of-a-thrown-exception-in-jest*/
			expect.assertions(2)
			try {
				actualGoal = makeGoal(-2, "#7EB2DD");
			} catch(ex) {
				expect(ex.message).toBe("baseline is outside acceptable range of values");
				expect(ex.name).toBe("RangeError");
			}
		});
		test("makeGoal() should throw a RangeError if too large a number is entered", () => {
			/*https://stackoverflow.com/questions/46042613/how-to-test-the-type-of-a-thrown-exception-in-jest*/
			expect.assertions(2)
			try {
				actualGoal = makeGoal(101, "#7EB2DD");
			} catch(ex) {
				expect(ex.message).toBe("baseline is outside acceptable range of values");
				expect(ex.name).toBe("RangeError");
			}
		});
		test("makeGoal() should throw a TypeError if nothing is entered", () => {
			/*https://stackoverflow.com/questions/46042613/how-to-test-the-type-of-a-thrown-exception-in-jest*/
			expect.assertions(2)
			try {
				actualGoal = makeGoal();
			} catch(ex) {
				expect(ex.message).toBe("baseline is not a number");
				expect(ex.name).toBe("TypeError");
			}
		});
		test("makeGoal() should return a goal - takes a colour", () => {
			expectedGoal = {
				name: "Baseline",
				value: 70,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: "#7EB2DD"
			};

			actualGoal = makeGoal(70, "#7EB2DD");

			expect(expectedGoal).toEqual(actualGoal);
		});
		test("makeGoal() should return a goal - takes a different colour", () => {
			expectedGoal = {
				name: "Baseline",
				value: 71,
				strokeWidth: 5,
				strokeHeight: 10, 
				strokeColor: "#F5853F"
			};

			actualGoal = makeGoal(71, "#F5853F");

			expect(expectedGoal).toEqual(actualGoal);
		});


	});
	/*Child test suite*/
	describe("Map Scores", () => {
		test("Map simple arrays should return a score object", () => {
			functions = ['First Function'];
			scores = [75];
			baseline = [25];

			expectedScore = {
				x: 'First Function',
				y: 75,
				goals: [{
					name: 'Baseline',
					value: 25,
					strokeWidth: 5,
					strokeHeight: 10,
					strokeColor: '#7EB2DD'
				}]
			};

			expect(mapScores(functions, scores, baseline)).toEqual(expectedScore);
		});
		test("Map simple arrays should return a 2nd score object", () => {
			functions = ['Second Function'];
			scores = [80];
			baseline = [35];

			expectedScore = {
				x: 'Second Function',
				y: 80,
				goals: [{
					name: 'Baseline',
					value: 35,
					strokeWidth: 5,
					strokeHeight: 10,
					strokeColor: '#7EB2DD'
				}]
			};

			expect(mapScores(functions, scores, baseline)).toEqual(expectedScore);
		});
		test("Combining arrays with 1 item each should return an array with 1 combined object", () => {
			let functions = ['Combine 1'];
			let scores = [50];
			let baseline = [10];

			expectedCombination = [{
				"function": "Combine 1",
				"score": 50,
				"baseline": 10
			}];

            let acutalCombination = combineScores(functions, scores, baseline);
            expect(acutalCombination.length).toBe(1);
			expect(acutalCombination).toEqual(expectedCombination);
		});
		test("Combining 2nd set of arrays with 1 item each should return an array with 1 combined object", () => {
			let functions = ['Combine 1'];
			let scores = [55];
			let baseline = [15];

			expectedCombination = [{
				"function": "Combine 1",
				"score": 55,
				"baseline": 15
			}];

            let acutalCombination = combineScores(functions, scores, baseline);
            expect(acutalCombination.length).toBe(1);
			expect(acutalCombination).toEqual(expectedCombination);
		});
		test("Combining arrays with 2 items each should return an array with 2 combined objects", () => {
			let functions = ['Combine 1', "Combine 2"];
			let scores = [55, 60];
			let baseline = [15, 20];

			expectedCombination = [
				{
					"function": "Combine 1",
					"score": 55,
					"baseline": 15
				},
				{
					"function": "Combine 2",
					"score": 60,
					"baseline": 20
				}
			];

            let acutalCombination = combineScores(functions, scores, baseline);
            expect(acutalCombination.length).toBe(2);
			expect(acutalCombination).toEqual(expectedCombination);
		});
		test("Combining arrays with 6 items each should return an array with 6 combined objects", () => {
			let functions = ["Task Behaviour", "Cognitive", "Motor Planning", "Motor", "Sensory Modulation", "Social / Emotional"];
			let scores = [20, 40, 60, 80, 100, 80];
			let baseline = [70, 70, 60, 68, 70, 72];

			expectedCombination = [
				{
					"function": "Task Behaviour",
					"score": 20,
					"baseline": 70
				},
				{
					"function": "Cognitive",
					"score": 40,
					"baseline": 70
				},
				{
					"function": "Motor Planning",
					"score": 60,
					"baseline": 60				},
				{
					"function": "Motor",
					"score": 80,
					"baseline": 68
				},
				{
					"function": "Sensory Modulation",
					"score": 100,
					"baseline": 70
				},
				{
					"function": "Social / Emotional",
					"score": 80,
					"baseline": 72
				}
			];
            
            let acutalCombination = combineScores(functions, scores, baseline);
            expect(acutalCombination.length).toBe(6);
			expect(acutalCombination).toEqual(expectedCombination);
		});
		test("Mapping function arrays with 1 item each should return a score object", () => {
			let functions = ["Map Function 1"];
			let scores = [55];
			let baselines = [15];
			let functionColours = {"baseline": "#7EB2DD"};

			expectedFunctionScore = [{
                x: "Map Function 1",
                y: 55,
                goals: [
                  {
                    name: "Baseline",
                    value: 15,
                    strokeWidth: 5,
                    strokeHeight: 10,
                    strokeColor: "#7EB2DD"
                  }
                ]
              }]

              let acutalFunctionScores = mapFunctionScores(functions, scores, baselines, functionColours);
              expect(acutalFunctionScores.length).toBe(1);
              expect(acutalFunctionScores).toEqual(expectedFunctionScore);

		});
		test("Mapping function arrays with 1 item each and a different colour should return a score object", () => {
			let functions = ["Map Function 1"];
			let scores = [55];
			let baselines = [15];
			let functionColours = {"baseline": "#F5853F"};

			expectedFunctionScore = [{
                x: "Map Function 1",
                y: 55,
                goals: [
                  {
                    name: "Baseline",
                    value: 15,
                    strokeWidth: 5,
                    strokeHeight: 10,
                    strokeColor: "#F5853F"
                  }
                ]
              }]

              let acutalFunctionScores = mapFunctionScores(functions, scores, baselines, functionColours);
              expect(acutalFunctionScores.length).toBe(1);
              expect(acutalFunctionScores).toEqual(expectedFunctionScore);

		});
		test("Mapping function arrays with 2 items each should return an array of 2 score objects", () => {
			let functions = ["Map Function 1", "Map Function 2"];
			let scores = [55, 65];
			let baselines = [15, 20];
			let functionColours = {"baseline": "#7EB2DD"};

			expectedFunctionScore = [{
                x: "Map Function 1",
                y: 55,
                goals: [
                  {
                    name: "Baseline",
                    value: 15,
                    strokeWidth: 5,
                    strokeHeight: 10,
                    strokeColor: "#7EB2DD"
                  }
                ]
              },
              {
                x: "Map Function 2",
                y: 65,
                goals: [
                  {
                    name: "Baseline",
                    value: 20,
                    strokeWidth: 5,
                    strokeHeight: 10,
                    strokeColor: "#7EB2DD"
                  }
                ]
              }]

              let acutalFunctionScores = mapFunctionScores(functions, scores, baselines, functionColours);
              expect(acutalFunctionScores.length).toBe(2);
              expect(acutalFunctionScores).toEqual(expectedFunctionScore);

		});
		test("Mapping function arrays with 6 items each should return an array of 6 score objects", () => {
			let functions = ["Task Behaviour", "Cognitive", "Motor Planning", "Motor", "Sensory Modulation", "Social / Emotional"];
			let scores = [20, 40, 60, 80, 100, 80];
			let baselines = [70, 70, 60, 68, 70, 72];
			let functionColours = {"baseline": "#7EB2DD"};

			expectedFunctionScores = [{
		                x: 'Task Behaviour',
		                y: 20,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Cognitive',
		                y: 40,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor Planning',
		                y: 60,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 60,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor',
		                y: 80,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 68,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Sensory Modulation',
		                y: 100,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Social / Emotional',
		                y: 80,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 72,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              }
		            ];

              let acutalFunctionScores = mapFunctionScores(functions, scores, baselines, functionColours);
              expect(acutalFunctionScores.length).toBe(6);
              expect(acutalFunctionScores).toEqual(expectedFunctionScores);

		});

	});
	/*Child test suite*/
	describe("Create all options for the chart", () => {

		test("Develop chart options from data", () => {
			let functions = ["Task Behaviour", "Cognitive", "Motor Planning", "Motor", "Sensory Modulation", "Social / Emotional"];
			let scores = [20, 40, 60, 80, 100, 80];
			let baselines = [70, 70, 60, 68, 70, 72];
			let functionColours = {"baseline": "#7EB2DD", "bar": "#F5853F", "label": "#3D2724"};

			let expectedOptions = {
		        series: [{
		          	name: "Latest",
		          	data: [{
		                x: 'Task Behaviour',
		                y: 20,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Cognitive',
		                y: 40,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor Planning',
		                y: 60,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 60,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor',
		                y: 80,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 68,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Sensory Modulation',
		                y: 100,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 70,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Social / Emotional',
		                y: 80,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 72,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              }
		            ]
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
		        colors: ["#F5853F"],
		        dataLabels: {
		          enabled: true,
		          textAnchor: "start",
		          style: {
		            colors: ["#3D2724"]
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
		        xaxis: { categories: functions, },
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
		            fillColors: ["#F5853F", "#7EB2DD"]
		          }
		        }

		    };

		    let scoreOptions = createOptions(functions, scores, baselines, functionColours);

		    expect(scoreOptions).not.toBeNull();
		    expect(scoreOptions).not.toBeInstanceOf(String);

		    expect(JSON.stringify(scoreOptions)).toEqual(JSON.stringify(expectedOptions));
		});
		test("Develop chart options from data with new values", () => {
			let functions = ["Task Behaviour", "Cognitive", "Motor Planning", "Motor", "Sensory Modulation", "Social / Emotional"];
			let scores = [10, 20, 30, 40, 50, 60];
			let baselines = [2, 12, 22, 32, 43, 52];
			let functionColours = {"baseline": "#7EB2DD", "bar": "#F5853F", "label": "#3D2724"};

			let expectedOptions = {
		        series: [{
		          	name: "Latest",
		          	data: [{
		                x: 'Task Behaviour',
		                y: 10,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 2,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Cognitive',
		                y: 20,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 12,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor Planning',
		                y: 30,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 22,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Motor',
		                y: 40,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 32,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Sensory Modulation',
		                y: 50,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 43,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              },
		              {
		                x: 'Social / Emotional',
		                y: 60,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 52,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: '#7EB2DD'
		                  }
		                ]
		              }
		            ]
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
		        colors: ["#F5853F"],
		        dataLabels: {
		          enabled: true,
		          textAnchor: "start",
		          style: {
		            colors: ["#3D2724"]
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
		        xaxis: { categories: functions, },
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
		            fillColors: ["#F5853F", "#7EB2DD"]
		          }
		        }

		    };

		    let scoreOptions = createOptions(functions, scores, baselines, functionColours);

		    expect(scoreOptions).not.toBeNull();
		    expect(scoreOptions).not.toBeInstanceOf(String);

		    expect(JSON.stringify(scoreOptions)).toEqual(JSON.stringify(expectedOptions));
		});
		test("should create chart options using different colours", () => {
			let functions = ["Task Behaviour", "Cognitive", "Motor Planning", "Motor", "Sensory Modulation", "Social / Emotional"];
			let scores = [10, 20, 30, 40, 50, 60];
			let baselines = [2, 12, 22, 32, 43, 52];
			let functionColours = {"baseline": "#0000FF", "label": "#FF0000", "bar": "#00FF00"};

			let expectedOptions = {
		        series: [{
		          	name: "Latest",
		          	data: [{
		                x: 'Task Behaviour',
		                y: 10,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 2,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              },
		              {
		                x: 'Cognitive',
		                y: 20,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 12,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              },
		              {
		                x: 'Motor Planning',
		                y: 30,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 22,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              },
		              {
		                x: 'Motor',
		                y: 40,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 32,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              },
		              {
		                x: 'Sensory Modulation',
		                y: 50,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 43,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              },
		              {
		                x: 'Social / Emotional',
		                y: 60,
		                goals: [
		                  {
		                    name: 'Baseline',
		                    value: 52,
		                    strokeWidth: 5,
		                    strokeHeight: 10,
		                    strokeColor: "#0000FF"
		                  }
		                ]
		              }
		            ]
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
		        colors: ["#00FF00"],
		        dataLabels: {
		          enabled: true,
		          textAnchor: "start",
		          style: {
		            colors: ["#FF0000"]
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
		        xaxis: { categories: functions, },
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
		            fillColors: ["#00FF00", "#0000FF"]
		          }
		        }

		    };

		    let scoreOptions = createOptions(functions, scores, baselines, functionColours);

		    expect(scoreOptions).not.toBeNull();
		    expect(scoreOptions).not.toBeInstanceOf(String);

		    expect(JSON.stringify(scoreOptions)).toEqual(JSON.stringify(expectedOptions));
		});

	});


});