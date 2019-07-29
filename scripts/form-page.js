function init() {
  // Urgency Levels
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_low","#urgency_low");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_medium", "#urgency_medium");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_high", "#urgency_high");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_urgent", "#urgency_urgent");

  //Tags

  //Row 1
  SetTagButtonToggle(".toggle_checkbox_holder_tag_vandalism", "#tag_vandalism");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_unsanitary","#tag_unsanitary");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_litter", "#tag_litter");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_landscaping_issue", "#tag_landscaping_issue");

  //Row 2
  SetTagButtonToggle(".toggle_checkbox_holder_tag_pollution", "#tag_pollution");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_structural_integrity", "#tag_structural_integrity");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_transportation_infrastructure", "#tag_transportation_infrastructure");
  SetTagButtonToggle(".toggle_checkbox_holder_tag_misc_maintenance", "#tag_misc_maintenance");
  //GetLocation();

  $('#loc_enter').click(onButtonClick);




  
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

function onButtonClick()
{
  loc = $('#address_textbox').val();

  $('#iframe_map').remove();

  $('#map').append('<iframe id = "iframe_map" width = "600" height = "450" frameborder = "0" style="border:0" src = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAxRqWmRH0WoaqkSYbLOMIg3roBnPJTqFo&q='+ loc + '" allowfullscreen></iframe>');
}

$(document).ready(init);
