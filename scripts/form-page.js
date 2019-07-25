function init() {
  // Urgency Levels
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_low","#urgency_low");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_medium", "#urgency_medium");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_high", "#urgency_high");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_urgency_urgent", "#urgency_urgent");

  //Tags
  SetUrgencyButtonToggle(".toggle_checkbox_holder_tag_vandalism", "#tag_vandalism");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_tag_drug","#tagtag_drug");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_tag_loitering", "#tag_loitering");
  SetUrgencyButtonToggle(".toggle_checkbox_holder_tag_underage_substance_use", "#tag_underage_substance_use");
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

$(document).ready(init);
