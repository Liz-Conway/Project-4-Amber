/*This jQuery code is only run after the HTML document has fully loaded*/
//https://api.jquery.com/ready/
$( domLoaded );

function domLoaded() {
	placeAccountLinks();
	/*Event listener to respond to a click on 
	the navigation link on mobile devices*/
	$(".navigationLink").on("click", closeNavigation);

	/*Add a diagnosis*/
	$("#diagnosisForm").submit(submitDiagnosis);
	/*Validate unique diagnosis*/
	$("#id_diagnosis").focusout(unfocusUnique);

	/*Set the date picker*/
	$(".dateInput").datepicker( {showAnim: "clip"} );
	
	/*Set the accordion element*/
	$("#accordion").accordion();
}

let unfocusUnique = (event) => validateUnique(event, "validateDiagnosis", "diagnosis", "#id_diagnosis");


/* Close the navigation panel on mobile devices
when a link is clicked*/
function closeNavigation(event) {
	$("#naviToggle").prop('checked', false);
}

/* Place the account links on the navigation panel
 - only on mobile devices*/
 function placeAccountLinks() {
 	/*Only needed for mobile devices - phones & tablets in portrait orientation*/
 	console.log("Screen width :  ", screen.width);
 	if (screen.width < 800) {
 		console.log("Setting location of #accountLinks");
 		$("#accountLinks").position({
  			my:      "top+30",
  			at:        "bottom",
 	   		of:        $("#navigationNav"),
   		 	collision: "none"
		});
 	} 
}


/*https://www.pluralsight.com/guides/work-with-ajax-django*/
/*
    On submiting the form, send the POST ajax
    request to server and after successful submission
    display the object.
*/
function submitDiagnosis(event) {
    // preventing from page reload and default actions
    event.preventDefault();
    // serialize the data for sending the form data.
    let serializedData = $(this).serialize();
    let newDiagnosis = $("#id_diagnosis").val();
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "",
        data: serializedData,
        success: function (response) {
        	console.log("Diagnosis successfully added");
            // on successfull creating object
            // 1. clear the form.
            //let newDiagnosis = $("#id_diagnosis").val();
            $("#diagnosisForm").trigger('reset');
            // 2. focus to diagnosis input 
            $("#id_diagnosis").focus();
            $("#id_diagnosis").val("");

            // display the new diagnosis in the list.
            let instance = JSON.parse(response["instance"]);
            let fields = instance[0]["fields"];
            $("#diagnosisList").append(
                `<li class="diagnosisItem">
                ${fields["diagnosis"]}
                </li>`
            )
            addMessage("success", "<span class='name'>" + newDiagnosis + "</span> diagnosis was added successfully");
        },
        error: function (response) {
        	console.log(response);
            // alert the error if any error occured
            // alert(response["responseJSON"]["error"]["diagnosis"]);
            console.log(response["responseJSON"]["error"]["diagnosis"]);
            //let newDiagnosis = $("#id_diagnosis").val();
            console.log("newDiagnosis :  ", newDiagnosis);
            let errorMessage = "";
            if (response["responseJSON"]["error"]["diagnosis"][0] === "Diagnosis with this Diagnosis already exists." ) {
            	errorMessage = "A Diagnosis of <span class='newEntry'>" + newDiagnosis + "</span> has already been added.<br>You cannot add a diagnosis with the same name.'";
            } else {
            	errorMessage = response["responseJSON"]["error"]["diagnosis"][0];
            }
            console.log("Error :  ", errorMessage);
            addMessage("error", errorMessage);
        }
    })
}


/*
On focus out on the add diagnosis field,
call AJAX get request to check if the diagnosis
already exists or not.
*/
function validateUnique(event, validUrl, fieldType, uniqueId) {
    console.log("validateUnique() called");
    event.preventDefault();
    // get the diagnosis entered
    let unique = $(uniqueId).val();
    console.log("Diagnosis entered :  ", unique);
    let dataObj = {};
    dataObj[fieldType] = unique;

    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: validUrl,
        data: dataObj,
        success: function (response) {
        	let duplicate = $(uniqueId).val();
        	console.log("Diagnosis entered (AJAX success()) :  ", unique);
        	console.log(response);

            // if not valid user, alert the user
            if(!response["valid"]){
                errorMessage = "A " + fieldType + " of '" + duplicate + "' has already been added.\nYou cannot add a " + fieldType + " with the same name.'";
                //alert(errorMessage);
                addMessage("error", errorMessage);
                let unique = $(uniqueId);
                unique.val("");
                unique.focus();
            }
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function addMessage(msgType, msg) {
	messageBlock();

	let uiState = "ui-state-";
	let state = "";

	switch(msgType) {
		case "success":
			state = "highlight";
			break;
		case "error":
			state = "error";
			break;
		default:
			state = "";
	}
	uiState += state;

	$("#messageBlock").empty();
	$("#messageBlock").append('<div class="message ' + uiState + '">' + msg + '</div>');
}

function messageBlock() {

	// If message block does not exist
	if (!$("#messageBlock").length ) {
		// Add a message block
		$("header.navigation").after('<div class="messages" id="messageBlock"></div>');
	}
}

