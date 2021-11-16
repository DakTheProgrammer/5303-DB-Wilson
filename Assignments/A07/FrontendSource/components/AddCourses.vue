<template>
  <div>
    <h1>{{ErrorMessage}}</h1>
    <PutOrPush style="display: inline-block" @getPutOrPush = "ChangeSen"/>
    <Dropdown @getDropdown= "ChangeSem"/>
    <br>
    <br>
    <Textbox message= "Crn" :maxLen="5" @getText = "ChangeCrn"/>
    <Textbox message= "College" :maxLen="2" @getText = "ChangeCol"/>
    <br>
    <br>
    <Textbox message= "Subject" :maxLen="4" @getText = "ChangeSub"/>
    <Textbox message= "Course#" :maxLen="4" @getText = "ChangeCor"/>
    <br>
    <br>
    <Textbox message= "Section" :maxLen="3" @getText = "ChangeSec"/>
    <Textbox message= "Title" :maxLen="100" @getText = "ChangeTit"/>
    <br>
    <br>
    <Textbox message= "Instructor" :maxLen="100" @getText = "ChangeIns"/>
    <Textbox message= "Size" :maxLen="3" @getText = "ChangeSiz"/>
    <br>
    <br>
    <Textbox message= "Current" :maxLen="3" @getText = "ChangeCur"/>
    <Textbox message= "Available" :maxLen="3" @getText = "ChangeAva"/>
    <br>
    <br>
    <Textbox message= "Days" :maxLen="5" @getText = "ChangeDay"/>
    <Textbox message= "Start" :maxLen="6" @getText = "ChangeSta"/>
    <br>
    <br>
    <Textbox message= "End" :maxLen="6" @getText = "ChangeEnd"/>
    <Textbox message= "Building" :maxLen="2" @getText = "ChangeBui"/>
    <br>
    <br>
    <Textbox message= "Room" :maxLen="10" @getText = "ChangeRoo"/>
    <Button @pressed= "Click"/>
  </div>

</template>

<script>
import Dropdown from "./Dropdown.vue"
import Textbox from "./Textbox.vue"
import Button from "./Button.vue"
import PutOrPush from './PutOrPush.vue'

export default {
  components:{
    Textbox,
    Dropdown,
    Button,
    PutOrPush
  },
  data(){
    return{
      ErrorMessage: "",
      Send: "New",
      Semester: "spring 2022",
      Crn: -400,
      Section: "",
      Title: "",
      Instructor: "",
      Size: "",
      Current: "",
      Available: "",
      Days: "",
      Start: "",
      End: "",
      College: "",
      Subject: "",
      Course: "",
      Building: "",
      Room: ""
    }
  },
  methods:{
    async Click() {
      if(this.Send == "New")
      {
        try
        {
          const options = {method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({
          "Semester": this.Semester,
          "Crn": this.Crn,
          "Section": this.Section,
          "Title": this.Title,
          "Instructor": this.Instructor,
          "Size": this.Size,
          "Current": this.Current,
          "Available": this.Available,
          "Days": this.Days,
          "Start": this.Start,
          "End": this.End,
          "College": this.College,
          "Subject": this.Subject,
          "Course#": this.Course,
          "Building": this.Building,
          "Room": this.Room})} 

          await fetch("http://167.99.6.44:8004/addcourse", options);
          //const response = await fetch("http://167.99.6.44:8004/addcourse", options);
          // const data = await response.json();
          this.ErrorMessage = "Success!"
        }
        catch
        {
          console.log('a');
          this.ErrorMessage = "Must give a unique Crn"
        }

        
      }
      else if(this.Send == "Update")
      {
        const sender = {method: "GET"} 

        const get = await fetch("http://167.99.6.44:8004/courseid/" + this.Crn + "/" + this.Semester, sender);
        const stuff = await get.json();

        if(stuff.result.length != 0)
        {
          const options = {method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify({
          "Semester": this.Semester,
          "Crn": this.Crn,
          "Section": this.Section,
          "Title": this.Title,
          "Instructor": this.Instructor,
          "Size": this.Size,
          "Current": this.Current,
          "Available": this.Available,
          "Days": this.Days,
          "Start": this.Start,
          "End": this.End,
          "College": this.College,
          "Subject": this.Subject,
          "Course#": this.Course,
          "Building": this.Building,
          "Room": this.Room})} 

          await fetch("http://167.99.6.44:8004/editcourse", options);
          // const response = await fetch("http://167.99.6.44:8004/editcourse", options);
          // const data = await response.json();
          this.ErrorMessage = "Success!"
        }
        else
        {
          this.ErrorMessage = "No Crn by that number"
        }
      }
      
    },
    ChangeCrn(value){
      this.Crn = value
    },
    ChangeSec(value){
      this.Section = value
    },
    ChangeTit(value){
      this.Title = value
    },
    ChangeIns(value){
      this.Instructor = value
    },
    ChangeSiz(value){
      this.Size = value
    },
    ChangeCur(value){
      this.Current = value
    },
    ChangeAva(value){
      this.Available = value
    },
    ChangeDay(value){
      this.Days = value
    },
    ChangeSta(value){
      this.Start = value
    },
    ChangeEnd(value){
      this.End = value
    },
    ChangeCol(value){
      this.College = value
    },
    ChangeSub(value){
      this.Subject = value
    },
    ChangeCor(value){
      this.Course = value
    },
    ChangeBui(value){
      this.Building = value
    },
    ChangeRoo(value){
      this.Room = value
    },
    ChangeSem(value)
    {
      this.Semester = value
    },
    ChangeSen(value)
    {
      this.Send = value
    }
  }
  
}
</script>

<style>
</style>
