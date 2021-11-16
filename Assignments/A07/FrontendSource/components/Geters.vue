<template>
    <div>
        <br>
        <h1>{{error}}</h1>
        <div id='glen'>
            <p id='x' class="q1">Crn</p>
            <p id='x' class="q2">Coll</p>
            <p id='x' class="q3">Subj</p>
            <p id='x' class="q4">Crs#</p>
            <p id='x' class="q5">Sec</p>
            <p id='x' class="q6">Tilte</p>
            <p id='x' class="q7">Instructor</p>
            <p id='x' class="q8">S</p>
            <p id='x' class="q9">C</p>
            <p id='x' class="q10">A</p>
            <p id='x' class="q11" style="height: 30px">Day</p>
            <p id='x' class="q12" style="height: 30px">Start</p>
            <p id='x' class="q13" style="height: 30px">End</p>
            <p id='x' class="q14" style="height: 30px">Bui</p>
            <p id='x' class="q15" style="height: 30px">Room</p>
        </div>
        <br>
        <div v-if="show">
          <template v-for="j in rows" :key="j.why">
              <template v-for="i in columns.length" :key="i.lol">
                  <div id='glen'>
                        <p id='v' class="q1" v-if="i % 15 == 1">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q2" v-if="i % 15 == 2">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q3" v-if="i % 15 == 3">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q4" v-if="i % 15 == 4">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q5" v-if="i % 15 == 5">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q6" v-if="i % 15 == 6">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q7" v-if="i % 15 == 7">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q8" v-if="i % 15 == 8">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q9" v-if="i % 15 == 9">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q10" v-if="i % 15 == 10">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q11" v-if="i % 15 == 11">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q12" v-if="i % 15 == 12">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q13" v-if="i % 15 == 13">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q14" v-if="i % 15 == 14">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='v' class="q15" v-if="i % 15 == 0">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                    </div>
              </template>
              <br>
          </template>
        </div>
    </div>
</template>

<script>

export default {
  components:{

  },
  data(){
    return{
        columns: [],
        result: [],
        rows: 0,
        show: false,
        error: ""
    }
  },
  props:{
    apiurl: String,
    test: Number
  },
  watch:{
    test: function()
    {
      this.ApiCall()
    }
  },
  methods:{
    async ApiCall()
    {
      try
      {
        this.error = ""
        this.show = false
        this.result = []
        //console.log(this.apiurl);
        const response = await fetch(this.apiurl);
        const data = await response.json();//data.result is an array
        this.columns = Object.keys(data.result[0])
        this.rows = data.result.length

        for(var i = 0; i < data.result.length; i++)
        {
          for(var j = 0; j < this.columns.length; j++)
          {
            this.result.push(data.result[i][this.columns[j]])
          }
        }
        this.show = true

        //console.log(data.result)
      }
      catch
      {
        this.error = "DOES NOT EXIST"
      }
    }
  },
  
}
</script>

<style>
#glen
{
  display: inline-flex;
  text-align: left;
}

#v
{
  display : inline;
  border-top:double;
}

.q1
{
  width: 45px;

}

.q2
{
  width: 30px;

}

.q3
{
  width: 55px;

}

.q4
{
  width: 40px;

}

.q5
{
  width: 30px;

}

.q6
{
  width: 150px;

}

.q7
{
  width: 100px;

}

.q8
{
  width: 18px;

}

.q9
{
  width: 18px;

}

.q10
{
  width: 18px;
  height: 18px;
}

.q11
{
  width: 55px;
  height: 18px;

}

.q12
{
  width: 60px;
  height: 18px;

}

.q13
{
  width: 60px;
  height: 18px;

}

.q14
{
  width: 30px;
  height: 18px;

}

.q15
{
  width: 43px;
  height: 18px;
  position: relative
}

</style>
