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
