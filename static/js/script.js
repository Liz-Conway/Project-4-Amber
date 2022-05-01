/*This jQuery code is only run after the HTML document has fully loaded*/
$(
	domLoaded
);

function domLoaded() {
	/*Event listener to respond to a click on 
	the navigation link on mobile devices*/
	$(".navigationLink").on("click", closeNavigation);
	placeAccountLinks();

	/*Add a diagnosis*/
	$("#diagnosisForm").submit(submitDiagnosis);
	/*Validate unique diagnosis*/
	$("#id_diagnosis").focusout(unfocusUnique);
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
  			my:      "left top",
  			at:        "left bottom",
 	   		of:        $("#navigationNav"),
   		 	collision: "fit"
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
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "",
        data: serializedData,
        success: function (response) {
        	console.log("Diagnosis successfully added");
            // on successfull creating object
            // 1. clear the form.
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
            location.reload();
        },
        error: function (response) {
        	console.log(response);
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]["diagnosis"]);
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
                alert("A " + fieldType + " of '" + duplicate + "' has already been added.\nYou cannot add a " + fieldType + " with the same name.'");
                let unique = $(uniqueId);
                unique.val("")
                unique.focus()
            }
        },
        error: function (response) {
            console.log(response)
        }
    })
}
