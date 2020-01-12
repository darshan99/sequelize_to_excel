/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
    return sequelize.define('address', {
      addr1: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'addr_1'
      },
      addr2: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'addr_2'
      },
      city: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'city'
      },
      state: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'state'
      },
      country: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'country'
      },
      faxPhone: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'fax_phone'
      },
      modemPhone: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'modem_phone'
      },
      phone: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'phone'
      },
      postalCode: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'postal_code'
      },
      createdAt: {
        type: DataTypes.DATE,
        allowNull: true,
        field: 'createdAt'
      },
      updatedAt: {
        type: DataTypes.DATE,
        allowNull: true,
        field: 'updatedAt'
      },
      addressCat: {
        type: DataTypes.STRING,
        allowNull: true,
        field: 'address_cat'
      },
      id: {
        type: DataTypes.BIGINT,
        allowNull: false,
        primaryKey: true,
        autoIncrement: true,
        field: 'id'
      },
      version: {
        type: DataTypes.INTEGER,
        allowNull: false,
        field: 'version',
        defaultValue:0
      },
      cityGeoLocId: {
        type: DataTypes.BIGINT,
        allowNull: true,
        references: {
          model: 'geo_loc',
          key: 'id'
        },
        field: 'city_geo_loc_id'
      }
    }, {
      tableName: 'address',
      version:true
    });
  };
  