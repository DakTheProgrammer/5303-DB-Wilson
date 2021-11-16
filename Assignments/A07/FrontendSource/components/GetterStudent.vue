<template>
    <div>
        <br>
        <h1>{{error}}</h1>
        <div id='glen'>
            <p id='t' class="z1">M#</p>
            <p id='t' class="z2">First</p>
            <p id='t' class="z3">Last</p>
            <p id='t' class="z4">classification</p>
            <p id='t' class="z5">Email</p>
            <p id='t' class="z6">GPA</p>
            <p id='t' class="z7">GitHub</p>
        </div>
        <br>
        <div v-if="show">
          <template v-for="j in rows" :key="j.why">
              <template v-for="i in columns.length" :key="i.lol">
                  <div id='glen'>
                        <p id='r' class="z1" v-if="i % 7 == 1">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z2" v-if="i % 7 == 2">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z3" v-if="i % 7 == 3">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z4" v-if="i % 7 == 4">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z5" v-if="i % 7 == 5">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z6" v-if="i % 7 == 6">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
                        <p id='r' class="z7" v-if="i % 7 == 0">{{result[(i - 1) + (columns.length * (j-1))]}}</p>
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
#r
{
    display: inline;
    border-bottom: double;
}

#t
{
    border-bottom: solid 1px;
}

.z1
{
    width: 100px;
    
}

.z2
{
  width: 130px;

}

.z3
{
  width: 130px;

}

.z4
{
  width: 100px;

}

.z5
{
  width: 250px;

}

.z6
{
  width: 40px;

}

.z7
{
  width: 100px;
}

</style>
