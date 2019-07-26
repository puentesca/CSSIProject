function init() {
  // Urgency Levels
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_low","#urgency_low");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_medium", "#urgency_medium");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_high", "#urgency_high");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_urgent", "#urgency_urgent");

  //Tags

  //Row 1
  SetTagButtonToggle(".toggle_checkbox_holder_tag_vandalism", "#tag_vandalism");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_drug","#tag_drug");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_loitering", "#tag_loitering");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_underage_substance_use", "#tag_underage_substance_use");

  //Row 2
  SetTagButtonToggle(".toggle_checkbox_holder_tag_public_indecency", "#tag_public_indecency");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_unsanitary","#tag_unsanitary");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_litter", "#tag_litter");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_biohazards", "#tag_biohazards");

  //Row 3
  SetTagButtonToggle(".toggle_checkbox_holder_tag_landscaping_issue", "#tag_landscaping_issue");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_pollution", "#tag_pollution");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_environmental_safety","#tag_environmental_safety");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_technical_connectivity", "#tag_technical_connectivity");

  //Row 4
  SetTagButtonToggle(".toggle_checkbox_holder_tag_structural_integrity", "#tag_structural_integrity");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_transportation_infrastructure", "#tag_transportation_infrastructure");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_accessibility","#tag_accessibility");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_misc_maintenance", "#tag_misc_maintenance");
  //GetLocation();
}

function SetUrgencyButtonToggle(div_name, checkbox_name)
{
  $(div_name).on("click", function() {
    if(UrgencySelected() && $(checkbox_name).is(':checked') != true)
      return;
    $(this).toggleClass("checkbox_on");
    $(checkbox_name).prop("checked", !$(checkbox_name).is(':checked'));
  });
}
// Returns true if an urgency is already selected
function UrgencySelected(){
  console.log("")
  let checkbox_names = ["#urgency_low","#urgency_medium", "#urgency_high","#urgency_urgent"]
  for(let i = 0; i < checkbox_names.length; i++)
  {
    let checkbox_name = checkbox_names[i];
    //If an urgency is already selected
    if($(checkbox_name).is(':checked'))
      return true;
  }
  return false;
}

function SetTagButtonToggle(div_name, checkbox_name)
{
  $(div_name).on("click", function() {
    $(this).toggleClass("checkbox_on");
    $(checkbox_name).prop("checked", !$(checkbox_name).is(':checked'));
  });
}

// function GetLocation()
// {
//   console.log("Called!");
//   var startPos;
//   var geoSuccess = function(position) {
//     startPos = position; document.getElementById('startLat').innerHTML = startPos.coords.latitude;
//     document.getElementById('startLon').innerHTML = startPos.coords.longitude;
//
//
//   };
//   console.log(navigator.geolocation.getCurrentPosition(geoSuccess));
// }

$(document).ready(init);
