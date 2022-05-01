/*This jQuery code is only run after the HTML document has fully loaded*/
$(
	domLoaded
);

function domLoaded() {
	/*Event listener to respond to a click on 
	the navigation link on mobile devices*/
	$(".navigationLink").on("click", closeNavigation);
	placeAccountLinks();
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

/*
    On submiting the form, send the POST ajax
    request to server and after successful submission
    display the object.
*/
$("#diagnosisForm").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
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

            // display the new diagnosis in the list.
            let instance = JSON.parse(response["instance"]);
            let fields = instance[0]["fields"];
            $("#diagnosisList").append(
                `<li>
                ${fields["diagnosis"]}
                </li>`
            )
        },
        error: function (response) {
        	console.log(response);
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]["diagnosis"]);
        }
    })
})


/*
On focus out on the add diagnosis field,
call AJAX get request to check if the diagnosis
already exists or not.
*/
$("#id_diagnosis").focusout(function (e) {
    e.preventDefault();
    // get the diagnosis entered
    let diagnosis = $(this).val();
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "validateDiagnosis",
        data: {"diagnosis": diagnosis},
        success: function (response) {
        	let duplicate = $("#id_diagnosis").val();
            // if not valid user, alert the user
            if(!response["valid"]){
                alert("A diagnosis of '" + duplicate + "' has already been added.\nYou cannot add a diagnosis with the same name.'");
                let diagnosis = $("#id_diagnosis");
                diagnosis.val("")
                diagnosis.focus()
            }
        },
        error: function (response) {
            console.log(response)
        }
    })
})
