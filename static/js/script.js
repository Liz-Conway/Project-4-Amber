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

	/*Set the date picker for editing a date*/
	$(".editDate > .dateInput").datepicker( {
		showAnim: "clip",
		changeMonth: true,
		changeYear: true,
		dateFormat: "dd/mm/yy",
		yearRange: "c-15:c+15"	// c-15 => 15 Years before existing date, TO c+15 => 15 years after existing date
	} );
	
	/*Set the date picker*/
	$(".dateInput").datepicker( {
		showAnim: "clip",
		changeMonth: true,
		changeYear: true,
		dateFormat: "dd/mm/yy",
		yearRange: "c-30:c+0"	// c-30 => 30 Years ago, TO c+0 => This year
	} );

	/*Set the accordion element*/
	$("#accordion").accordion();

	/*Set a handler for when the window is resized
	 * Replace the Account Links div*/
	$( window ).resize(placeAccountLinks);

}

/* Close the navigation panel on mobile devices
when a link is clicked*/
function closeNavigation(event) {
	$("#naviToggle").prop('checked', false);
}

/* Place the account links on the navigation panel
 - only on mobile devices*/
 function placeAccountLinks() {
 	/*Only needed for mobile devices - phones & tablets in portrait orientation*/
 	/*Use screen width instead of window width since 
 	the media queries use screen width*/
 	if (screen.width < 800) {
 		$("#accountLinks").position({
  			my:      "top+20",
  			at:        "bottom",
 	   		of:        $("#navigationNav"),
   		 	collision: "fit"
		});
 	} else {
		$("#accountLinks").position({
  			my:      "right top",
  			at:        "right top",
 	   		of:        $("#navWrapper"),
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
    // serialize the data for sending the form data to the database.
    let serializedData = $(this).serialize();
    let newDiagnosis = $("#id_diagnosis").val();
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "",
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            // 1. clear the form.
            $("#diagnosisForm").trigger('reset');
            // 2. focus to diagnosis input 
            $("#id_diagnosis").focus();
            $("#id_diagnosis").val("");

            // display the new diagnosis in the list.
            let instance = JSON.parse(response.instance);
            let fields = instance[0].fields;
            $("#diagnosisList").append(
                `<li class="diagnosisItem">
                ${fields["diagnosis"]}
                </li>`
            )
            addMessage("success", "<span class='name'>" + newDiagnosis + "</span> diagnosis was added successfully");
        },
        error: function (response) {
            let errorMessage = "";
            if (response["responseJSON"]["error"]["diagnosis"][0] === "Diagnosis with this Diagnosis already exists." ) {
            	errorMessage = "A Diagnosis of <span class='newEntry'>" + newDiagnosis + "</span> has already been added.<br>You cannot add a diagnosis with the same name.'";
            } else {
            	errorMessage = response["responseJSON"]["error"]["diagnosis"][0];
            }
            addMessage("error", errorMessage);
        }
    })
}

function addMessage(msgType, msg) {

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

function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

function selectClient(clientID) {
	let chosen = $("#chosenClient");
	chosen.val(clientID);
	$("#selectClientForm").submit();
}
