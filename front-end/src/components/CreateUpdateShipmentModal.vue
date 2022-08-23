<template>
    <b-modal
      :id="mode"
      ref="modal"
      title="Create Shipment"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="shipping_address"
          label-for="shipping-address-input"
        >
          <b-form-input
            id="shipping-address-input"
            v-model="shipment.shipping_address"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="biling_address"
          label-for="biling-address-input"
        >
          <b-form-input
            id="biling-address-input"
            v-model="shipment.biling_address"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="product_price"
          label-for="product-price-input"
        >
          <b-form-input
            id="product-price-input"
            type="number"
            v-model="shipment.product_price"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="delivery_cost"
          label-for="delivery-cost-input"
        >
          <b-form-input
            id="delivery-cost-input"
            type="number"
            v-model="shipment.delivery_cost"
            required
          ></b-form-input>
        </b-form-group>
         <b-form-group
          label="final_price"
          label-for="final-price-input"
        >
          <b-form-input
            id="final-price-input"
            type="number"
            v-model="shipment.final_price"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
</template>

<script>
export default {
    name: 'CreateUpdateShipmentModal',
    props: {
        mode: {
            type: String,
            default: () => 'create'
        },
        shipment: {
            type: Object,
            default: () => ({
                id: null,
                shipping_address: '',
                biling_address: '',
                product_price: '',
                delivery_cost: '',
                final_price: '',
                actions: ''
            })
        },
    },
    data() {
      return {
        name: '',
      }
    },
    computed: {
        isCreate() {
            return this.mode === 'create'
        }
    },
    methods: {
      resetModal() {
        this.shipment.id = null
        this.shipment.shipping_address = ''
        this.shipment.biling_address = ''
        this.shipment.product_price = ''
        this.shipment.delivery_cost = ''
        this.shipment.final_price = ''
      },
      handleOk(bvModalEvent) {
        // Prevent modal from closing
        bvModalEvent.preventDefault()
        // Trigger submit handler
        this.handleSubmit()
      },
      handleSubmit() {
        const promise = this.isCreate
            ? this.axios.post('api/shipments/', this.shipment)
            : this.axios.put(`api/shipments/${this.shipment.id}/`, this.shipment)

        promise.finally(() => {          
          this.$bvModal.hide(this.mode)
          this.$emit('submit')
        })
      }
    }
  }
</script>

<style>

</style>