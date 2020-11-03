<template>
  <div id="app">
    <h4>User</h4>
    <div>
      <table>
        <tr>
          <th>Name</th>
          <th>
            {{ allSelected }}
            <input type="checkbox" @change="selectAll" v-model="allSelected" />
          </th>
        </tr>
        <tr v-for="user in users" :key="user">
          <td>{{ user.name }}</td>
          <td>
            <input
              type="checkbox"
              v-model="selected"
              :value="user.id"
            />
          </td>
        </tr>
      </table>
    </div>

    <span>Selected Ids: {{ selected }}</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [
        { id: "Shad", name: "Shad" },
        { id: "Duane", name: "Duane" },
        { id: "Myah", name: "Myah" },
        { id: "Kamron", name: "Kamron" },
        { id: "Brendon", name: "Brendon" }
      ],
    //   selected: [],
      allSelected: false,
      selected: []
    };
  },
  watch: {
		"selected": function() {
			if (this.selected.length == this.users.length) {
                this.allSelected = true
			} else {
				this.allSelected = false
			}
		}
	},
  methods: {
    selectAll: function() {
      this.selected = [];
        if (this.allSelected) {
            for (let index = 0; index < this.users.length; index++) {
        this.selected.push(this.users[index].id.toString());
        }
        // this.selected = this.users
        } else {
            this.selected = []
        }
        
    },
    // select: function() {
    //   this.allSelected = false;
    // }
  },
  
};
</script>
