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
            :state="!errors.shipping_address"
            aria-describedby="input-live-help input-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="shipping-address-input">
            <span v-for="(error, index) in errors.shipping_address" :key="index">
              {{error}}
            </span>
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          label="biling_address"
          label-for="biling-address-input"
        >
          <b-form-input
            id="biling-address-input"
            v-model="shipment.biling_address"
            :state="!errors.biling_address"
            aria-describedby="input-live-help input-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="biling-address-input">
            <span v-for="(error, index) in errors.biling_address" :key="index">
              {{error}}
            </span>
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          label="product_price"
          label-for="product-price-input"
        >
          <b-form-input
            id="product-price-input"
            type="number"
            v-model="shipment.product_price"
            :state="!errors.product_price"
            aria-describedby="input-live-help input-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="product-price-input">
            <span v-for="(error, index) in errors.product_price" :key="index">
              {{error}}
            </span>
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          label="delivery_cost"
          label-for="delivery-cost-input"
        >
          <b-form-input
            id="delivery-cost-input"
            type="number"
            v-model="shipment.delivery_cost"
            :state="!errors.delivery_cost"
            aria-describedby="input-live-help input-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="delivery-cost-input">
            <span v-for="(error, index) in errors.delivery_cost" :key="index">
              {{error}}
            </span>
          </b-form-invalid-feedback>
        </b-form-group>
         <b-form-group
          label="final_price"
          label-for="final-price-input"
        >
          <b-form-input
            id="final-price-input"
            type="number"
            v-model="shipment.final_price"
            :state="!errors.final_price"
            aria-describedby="input-live-help input-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="final-price-input">
            <span v-for="(error, index) in errors.final_price" :key="index">
              {{error}}
            </span>
          </b-form-invalid-feedback>
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
        errors: {}
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
        this.errors = {}
        const promise = this.isCreate
            ? this.axios.post('api/shipments/', this.shipment)
            : this.axios.put(`api/shipments/${this.shipment.id}/`, this.shipment)


        promise.then(() => {          
          this.$bvModal.hide(this.mode)
          this.$emit('submit')
        })
        promise.catch((error) => {
          this.errors = error.response.data
        })
      }
    }
  }
</script>

<style>

</style>