<template id='app'>
  <div>
    <br>
    <div id = 'selector'>
      <p id = 'title'>Select</p>
          <select name='option' v-model="Selected" @change="SetIf">
              <option value="Add/Update course">Add/Update course</option>
              <option value="Add/Update form">Add/Update form</option>
              <option value="Add/Update student">Add/Update student</option>
              <option value="Find course by crn">Find course by crn</option>
              <option value="Find course by building">Find course by building</option>
              <option value="Find closed courses">Find closed courses</option>
              <option value="Find course by course number">Find course by course number</option>
              <option value="Find course by professor">Find course by professor</option>
              <option value="Find course by subject">Find course by subject</option>
              <option value="Find course by time">Find course by time</option>
              <option value="Find all forms">Find all forms</option>
              <option value="Find forms from semester">Find forms from semester</option>
              <option value="Find forms from a student by M#">Find forms from a student by M#</option>
              <option value="Find forms from a student by M# and semester">Find forms from a student by M# and semeseter</option>
              <option value="Find forms from a student by M# and year">Find forms from a student by M# and year</option>
              <option value="Find forms from a year">Find forms from a year</option>
              <option value="Find students from a semester">Find students from a semester</option>
              <option value="Find students with a higher gpa">Find students with a higher gpa</option>
              <option value="Find students with a lower gpa">Find students with a lower gpa</option>
              <option value="Find students with given name">Find students with given name</option>
              <option value="Find students with given M#">Find students with given M#</option>
              <option value="Find students with given gpa">Find students with given gpa</option>
          </select>
      </div>

    <div id='form' v-if="shower">
      <AddCourses v-if="Shows[0]"/>
      <AddForms v-if="Shows[1]"/>
      <AddStudnets v-if="Shows[2]"/>

      <GetCourseId v-if="Shows[3]"/>
      <GetCourseBuilding v-if="Shows[4]"/>
      <GetCourseClosed v-if="Shows[5]"/>
      <GetCourseNum v-if="Shows[6]"/>
      <GetCourseProf v-if="Shows[7]"/>
      <GetCourseSubject v-if="Shows[8]"/>
      <GetCourseTime v-if="Shows[9]"/>

      <GetForms v-if="Shows[10]"/>
      <GetFormsSemester v-if="Shows[11]"/>
      <GetFormsStudent v-if="Shows[12]"/>
      <GetFormsStudentSemster v-if="Shows[13]"/>
      <GetFormsStudentYear v-if="Shows[14]"/>
      <GetFormsYear v-if="Shows[15]"/>

      <GetStudents v-if="Shows[16]"/>
      <GetStudentsGpaHigher v-if="Shows[17]"/>
      <GetStudentsGpaLower v-if="Shows[18]"/>
      <GetStudentsName v-if="Shows[19]"/>
      <GetStudentsNum v-if="Shows[20]"/>
      <GetStudentsWithGpa v-if="Shows[21]"/>
      
    </div>
    <br>
  </div>

</template>

<script>
import AddForms from './components/AddForms.vue'
import AddCourses from './components/AddCourses.vue'
import AddStudnets from './components/AddStudnets.vue'
import GetCourseId from './components/GetCourseId.vue'
import GetCourseBuilding from './components/GetCourseBuilding.vue'
import GetCourseClosed from './components/GetCourseClosed.vue'
import GetCourseNum from './components/GetCourseNum.vue'
import GetCourseProf from './components/GetCourseProf.vue'
import GetCourseSubject from './components/GetCourseSubject.vue'
import GetCourseTime from './components/GetCourseTime.vue'
import GetStudents from './components/GetStudents.vue'
import GetStudentsGpaHigher from './components/GetStudentsGpaHigher.vue'
import GetStudentsGpaLower from './components/GetStudentsGpaLower.vue'
import GetStudentsWithGpa from './components/GetStudentsWithGpa.vue'
import GetStudentsName from './components/GetStudentsName.vue'
import GetStudentsNum from './components/GetStudentsNum.vue'
import GetFormsSemester from './components/GetFormsSemester.vue'
import GetFormsStudentSemster from './components/GetFormsStudentSemster.vue'
import GetForms from './components/GetForms.vue'
import GetFormsStudent from './components/GetFormsStudent.vue'
import GetFormsStudentYear from './components/GetFormsStudentYear.vue'
import GetFormsYear from './components/GetFormsYear.vue'

export default {
  components:{
    AddForms,
    AddCourses,
    AddStudnets,
    GetCourseId,
    GetCourseBuilding,
    GetCourseClosed,
    GetCourseNum,
    GetCourseProf,
    GetCourseSubject,
    GetCourseTime,
    GetStudents,
    GetStudentsGpaHigher,
    GetStudentsGpaLower,
    GetStudentsWithGpa,
    GetStudentsName,
    GetStudentsNum,
    GetFormsSemester,
    GetFormsStudentSemster,
    GetForms,
    GetFormsStudent,
    GetFormsStudentYear,
    GetFormsYear,
  },
  data(){
    return{
      Shows: [22],
      shower: false,
      Selected: ""
    }
  },
  created()
  {
    this.resetAll()
  },
  methods:{
    SetIf()
    {
      this.shower = true
      if(this.Selected == "Add/Update course")
      {
        this.resetAll()
        this.Shows[0] = true
      }
      else if(this.Selected == "Add/Update form")
      {
        this.resetAll()
        this.Shows[1] = true
      }
      else if(this.Selected == "Add/Update student")
      {
        this.resetAll()
        this.Shows[2] = true
      }
      else if(this.Selected == "Find course by crn")
      {
        this.resetAll()
        this.Shows[3] = true
      }
      else if(this.Selected == "Find course by building")
      {
        this.resetAll()
        this.Shows[4] = true
      }
      else if(this.Selected == "Find closed courses")
      {
        this.resetAll()
        this.Shows[5] = true
      }
      else if(this.Selected == "Find course by course number")
      {
        this.resetAll()
        this.Shows[6] = true
      }
      else if(this.Selected == "Find course by professor")
      {
        this.resetAll()
        this.Shows[7] = true
      }
      else if(this.Selected == "Find course by subject")
      {
        this.resetAll()
        this.Shows[8] = true
      }
      else if(this.Selected == "Find course by time")
      {
        this.resetAll()
        this.Shows[9] = true
      }
      else if(this.Selected == "Find all forms")
      {
        this.resetAll()
        this.Shows[10] = true
      }
      else if(this.Selected == "Find forms from semester")
      {
        this.resetAll()
        this.Shows[11] = true
      }
      else if(this.Selected == "Find forms from a student by M#")
      {
        this.resetAll()
        this.Shows[12] = true
      }
      else if(this.Selected == "Find forms from a student by M# and semester")
      {
        this.resetAll()
        this.Shows[13] = true
      }
      else if(this.Selected == "Find forms from a student by M# and year")
      {
        this.resetAll()
        this.Shows[14] = true
      }
      else if(this.Selected == "Find forms from a year")
      {
        this.resetAll()
        this.Shows[15] = true
      }
      else if(this.Selected == "Find students from a semester")
      {
        this.resetAll()
        this.Shows[16] = true
      }
      else if(this.Selected == "Find students with a higher gpa")
      {
        this.resetAll()
        this.Shows[17] = true
      }
      else if(this.Selected == "Find students with a lower gpa")
      {
        this.resetAll()
        this.Shows[18] = true
      }
      else if(this.Selected == "Find students with given name")
      {
        this.resetAll()
        this.Shows[19] = true
      }
      else if(this.Selected == "Find students with given M#")
      {
        this.resetAll()
        this.Shows[20] = true
      }
      else if(this.Selected == "Find students with given gpa")
      {
        this.resetAll()
        this.Shows[21] = true
      }
    },
    resetAll()
    {
      for(var i = 0; i < 22; i++)
      {
        this.Shows[i] = false
      }
    }
  }
}
</script>

<style>
body
{
  background-image: repeating-linear-gradient(90deg, #ffd900c4, #e0a400c4, #c06d00be, #800000be, #400000be);
	background-size: 400% 400%;
  animation: gradient 11s ease infinite; 
	height: 100vh;
  
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

#app, option, select
{
  color: #747474;
}

#selector
{
  background-color: white;
  text-align: center;
  padding-bottom: 2%;
  border-radius: 25px;
  width: 400px;
  margin-left: 30%;
}

#title
{
  text-align: left;
  position: relative;
  top: 20px;
  left: 25px;
}

select
{
  border-radius: 25px;
  border-color: #800000be;
  border-width: 3px;
}

#form
{
  background-color: white;
  text-align: center;
  border-color: black;
  margin-top: 2%;
  padding-top: 2%;
  padding-bottom: 2%;
  border-radius: 25px;
  width: 850px;
  margin-left: 5%;
}

</style>
