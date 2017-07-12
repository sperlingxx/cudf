# auto-generated file
import _cffi_backend

ffi = _cffi_backend.FFI('libgdf_cffi.libgdf_cffi',
    _version = 0x2601,
    _types = b'\x00\x00\x48\x0D\x00\x00\x01\x0B\x00\x00\x00\x0F\x00\x00\x48\x0D\x00\x00\x50\x03\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x4C\x03\x00\x00\x4A\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x4B\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x4D\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x4E\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x55\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x07\x11\x00\x00\x25\x11\x00\x00\x52\x03\x00\x00\x1C\x01\x00\x00\x00\x0B\x00\x00\x00\x0F\x00\x00\x4F\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x4E\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x04\x0D\x00\x00\x51\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x00\x0F\x00\x00\x53\x0D\x00\x00\x00\x0F\x00\x00\x54\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x55\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x55\x0D\x00\x00\x04\x11\x00\x00\x36\x11\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x49\x03\x00\x00\x02\x01\x00\x00\x0E\x01\x00\x00\x0D\x01\x00\x00\x01\x09\x00\x00\x15\x01\x00\x00\x17\x01\x00\x00\x07\x01\x00\x00\x00\x09\x00\x00\x12\x01\x00\x00\x04\x01\x00\x00\x08\x01\x00\x00\x55\x03\x00\x00\x00\x01',
    _globals = (b'\xFF\xFF\xFF\x0BGDF_COLUMN_SIZE_MISMATCH',3,b'\xFF\xFF\xFF\x0BGDF_CUDA_ERROR',1,b'\xFF\xFF\xFF\x0BGDF_FLOAT32',5,b'\xFF\xFF\xFF\x0BGDF_FLOAT64',6,b'\xFF\xFF\xFF\x0BGDF_INT16',2,b'\xFF\xFF\xFF\x0BGDF_INT32',3,b'\xFF\xFF\xFF\x0BGDF_INT64',4,b'\xFF\xFF\xFF\x0BGDF_INT8',1,b'\xFF\xFF\xFF\x0BGDF_SUCCESS',0,b'\xFF\xFF\xFF\x0BGDF_UNSUPPORTED_DTYPE',2,b'\xFF\xFF\xFF\x0BGDF_VALIDITY_MISSING',4,b'\xFF\xFF\xFF\x0BGDF_invalid',0,b'\x00\x00\x10\x23gdf_acos_f32',0,b'\x00\x00\x10\x23gdf_acos_f64',0,b'\x00\x00\x10\x23gdf_acos_generic',0,b'\x00\x00\x14\x23gdf_add_f32',0,b'\x00\x00\x14\x23gdf_add_f64',0,b'\x00\x00\x14\x23gdf_add_generic',0,b'\x00\x00\x14\x23gdf_add_i32',0,b'\x00\x00\x14\x23gdf_add_i64',0,b'\x00\x00\x10\x23gdf_asin_f32',0,b'\x00\x00\x10\x23gdf_asin_f64',0,b'\x00\x00\x10\x23gdf_asin_generic',0,b'\x00\x00\x10\x23gdf_atan_f32',0,b'\x00\x00\x10\x23gdf_atan_f64',0,b'\x00\x00\x10\x23gdf_atan_generic',0,b'\x00\x00\x14\x23gdf_bitwise_and_generic',0,b'\x00\x00\x14\x23gdf_bitwise_and_i32',0,b'\x00\x00\x14\x23gdf_bitwise_and_i64',0,b'\x00\x00\x14\x23gdf_bitwise_and_i8',0,b'\x00\x00\x14\x23gdf_bitwise_or_generic',0,b'\x00\x00\x14\x23gdf_bitwise_or_i32',0,b'\x00\x00\x14\x23gdf_bitwise_or_i64',0,b'\x00\x00\x14\x23gdf_bitwise_or_i8',0,b'\x00\x00\x14\x23gdf_bitwise_xor_generic',0,b'\x00\x00\x14\x23gdf_bitwise_xor_i32',0,b'\x00\x00\x14\x23gdf_bitwise_xor_i64',0,b'\x00\x00\x14\x23gdf_bitwise_xor_i8',0,b'\x00\x00\x10\x23gdf_cast_f32_to_f32',0,b'\x00\x00\x10\x23gdf_cast_f32_to_f64',0,b'\x00\x00\x10\x23gdf_cast_f32_to_i32',0,b'\x00\x00\x10\x23gdf_cast_f32_to_i64',0,b'\x00\x00\x10\x23gdf_cast_f32_to_i8',0,b'\x00\x00\x10\x23gdf_cast_f64_to_f32',0,b'\x00\x00\x10\x23gdf_cast_f64_to_f64',0,b'\x00\x00\x10\x23gdf_cast_f64_to_i32',0,b'\x00\x00\x10\x23gdf_cast_f64_to_i64',0,b'\x00\x00\x10\x23gdf_cast_f64_to_i8',0,b'\x00\x00\x10\x23gdf_cast_generic_to_f32',0,b'\x00\x00\x10\x23gdf_cast_generic_to_f64',0,b'\x00\x00\x10\x23gdf_cast_generic_to_i32',0,b'\x00\x00\x10\x23gdf_cast_generic_to_i64',0,b'\x00\x00\x10\x23gdf_cast_generic_to_i8',0,b'\x00\x00\x10\x23gdf_cast_i32_to_f32',0,b'\x00\x00\x10\x23gdf_cast_i32_to_f64',0,b'\x00\x00\x10\x23gdf_cast_i32_to_i32',0,b'\x00\x00\x10\x23gdf_cast_i32_to_i64',0,b'\x00\x00\x10\x23gdf_cast_i32_to_i8',0,b'\x00\x00\x10\x23gdf_cast_i64_to_f32',0,b'\x00\x00\x10\x23gdf_cast_i64_to_f64',0,b'\x00\x00\x10\x23gdf_cast_i64_to_i32',0,b'\x00\x00\x10\x23gdf_cast_i64_to_i64',0,b'\x00\x00\x10\x23gdf_cast_i64_to_i8',0,b'\x00\x00\x10\x23gdf_cast_i8_to_f32',0,b'\x00\x00\x10\x23gdf_cast_i8_to_f64',0,b'\x00\x00\x10\x23gdf_cast_i8_to_i32',0,b'\x00\x00\x10\x23gdf_cast_i8_to_i64',0,b'\x00\x00\x10\x23gdf_cast_i8_to_i8',0,b'\x00\x00\x10\x23gdf_ceil_f32',0,b'\x00\x00\x10\x23gdf_ceil_f64',0,b'\x00\x00\x10\x23gdf_ceil_generic',0,b'\x00\x00\x39\x23gdf_column_sizeof',0,b'\x00\x00\x28\x23gdf_column_view',0,b'\x00\x00\x10\x23gdf_cos_f32',0,b'\x00\x00\x10\x23gdf_cos_f64',0,b'\x00\x00\x10\x23gdf_cos_generic',0,b'\x00\x00\x14\x23gdf_div_f32',0,b'\x00\x00\x14\x23gdf_div_f64',0,b'\x00\x00\x14\x23gdf_div_generic',0,b'\x00\x00\x14\x23gdf_eq_f32',0,b'\x00\x00\x14\x23gdf_eq_f64',0,b'\x00\x00\x14\x23gdf_eq_generic',0,b'\x00\x00\x14\x23gdf_eq_i32',0,b'\x00\x00\x14\x23gdf_eq_i64',0,b'\x00\x00\x14\x23gdf_eq_i8',0,b'\x00\x00\x00\x23gdf_error_get_name',0,b'\x00\x00\x10\x23gdf_exp_f32',0,b'\x00\x00\x10\x23gdf_exp_f64',0,b'\x00\x00\x10\x23gdf_exp_generic',0,b'\x00\x00\x10\x23gdf_floor_f32',0,b'\x00\x00\x10\x23gdf_floor_f64',0,b'\x00\x00\x10\x23gdf_floor_generic',0,b'\x00\x00\x14\x23gdf_floordiv_f32',0,b'\x00\x00\x14\x23gdf_floordiv_f64',0,b'\x00\x00\x14\x23gdf_floordiv_generic',0,b'\x00\x00\x14\x23gdf_floordiv_i32',0,b'\x00\x00\x14\x23gdf_floordiv_i64',0,b'\x00\x00\x14\x23gdf_ge_f32',0,b'\x00\x00\x14\x23gdf_ge_f64',0,b'\x00\x00\x14\x23gdf_ge_generic',0,b'\x00\x00\x14\x23gdf_ge_i32',0,b'\x00\x00\x14\x23gdf_ge_i64',0,b'\x00\x00\x14\x23gdf_ge_i8',0,b'\x00\x00\x14\x23gdf_gt_f32',0,b'\x00\x00\x14\x23gdf_gt_f64',0,b'\x00\x00\x14\x23gdf_gt_generic',0,b'\x00\x00\x14\x23gdf_gt_i32',0,b'\x00\x00\x14\x23gdf_gt_i64',0,b'\x00\x00\x14\x23gdf_gt_i8',0,b'\x00\x00\x40\x23gdf_ipc_parser_close',0,b'\x00\x00\x2F\x23gdf_ipc_parser_failed',0,b'\x00\x00\x3D\x23gdf_ipc_parser_get_data',0,b'\x00\x00\x32\x23gdf_ipc_parser_get_data_offset',0,b'\x00\x00\x03\x23gdf_ipc_parser_get_error',0,b'\x00\x00\x03\x23gdf_ipc_parser_get_layout_json',0,b'\x00\x00\x03\x23gdf_ipc_parser_get_schema_json',0,b'\x00\x00\x35\x23gdf_ipc_parser_open',0,b'\x00\x00\x43\x23gdf_ipc_parser_open_recordbatches',0,b'\x00\x00\x03\x23gdf_ipc_parser_to_json',0,b'\x00\x00\x14\x23gdf_le_f32',0,b'\x00\x00\x14\x23gdf_le_f64',0,b'\x00\x00\x14\x23gdf_le_generic',0,b'\x00\x00\x14\x23gdf_le_i32',0,b'\x00\x00\x14\x23gdf_le_i64',0,b'\x00\x00\x14\x23gdf_le_i8',0,b'\x00\x00\x10\x23gdf_log_f32',0,b'\x00\x00\x10\x23gdf_log_f64',0,b'\x00\x00\x10\x23gdf_log_generic',0,b'\x00\x00\x14\x23gdf_lt_f32',0,b'\x00\x00\x14\x23gdf_lt_f64',0,b'\x00\x00\x14\x23gdf_lt_generic',0,b'\x00\x00\x14\x23gdf_lt_i32',0,b'\x00\x00\x14\x23gdf_lt_i64',0,b'\x00\x00\x14\x23gdf_lt_i8',0,b'\x00\x00\x0B\x23gdf_max_f32',0,b'\x00\x00\x06\x23gdf_max_f64',0,b'\x00\x00\x23\x23gdf_max_generic',0,b'\x00\x00\x19\x23gdf_max_i32',0,b'\x00\x00\x1E\x23gdf_max_i64',0,b'\x00\x00\x0B\x23gdf_min_f32',0,b'\x00\x00\x06\x23gdf_min_f64',0,b'\x00\x00\x23\x23gdf_min_generic',0,b'\x00\x00\x19\x23gdf_min_i32',0,b'\x00\x00\x1E\x23gdf_min_i64',0,b'\x00\x00\x14\x23gdf_mul_f32',0,b'\x00\x00\x14\x23gdf_mul_f64',0,b'\x00\x00\x14\x23gdf_mul_generic',0,b'\x00\x00\x14\x23gdf_mul_i32',0,b'\x00\x00\x14\x23gdf_mul_i64',0,b'\x00\x00\x14\x23gdf_ne_f32',0,b'\x00\x00\x14\x23gdf_ne_f64',0,b'\x00\x00\x14\x23gdf_ne_generic',0,b'\x00\x00\x14\x23gdf_ne_i32',0,b'\x00\x00\x14\x23gdf_ne_i64',0,b'\x00\x00\x14\x23gdf_ne_i8',0,b'\x00\x00\x0B\x23gdf_product_f32',0,b'\x00\x00\x06\x23gdf_product_f64',0,b'\x00\x00\x23\x23gdf_product_generic',0,b'\x00\x00\x19\x23gdf_product_i32',0,b'\x00\x00\x1E\x23gdf_product_i64',0,b'\x00\x00\x3B\x23gdf_reduce_optimal_output_size',0,b'\x00\x00\x10\x23gdf_sin_f32',0,b'\x00\x00\x10\x23gdf_sin_f64',0,b'\x00\x00\x10\x23gdf_sin_generic',0,b'\x00\x00\x10\x23gdf_sqrt_f32',0,b'\x00\x00\x10\x23gdf_sqrt_f64',0,b'\x00\x00\x10\x23gdf_sqrt_generic',0,b'\x00\x00\x14\x23gdf_sub_f32',0,b'\x00\x00\x14\x23gdf_sub_f64',0,b'\x00\x00\x14\x23gdf_sub_generic',0,b'\x00\x00\x14\x23gdf_sub_i32',0,b'\x00\x00\x14\x23gdf_sub_i64',0,b'\x00\x00\x0B\x23gdf_sum_f32',0,b'\x00\x00\x06\x23gdf_sum_f64',0,b'\x00\x00\x23\x23gdf_sum_generic',0,b'\x00\x00\x19\x23gdf_sum_i32',0,b'\x00\x00\x1E\x23gdf_sum_i64',0,b'\x00\x00\x0B\x23gdf_sum_squared_f32',0,b'\x00\x00\x06\x23gdf_sum_squared_f64',0,b'\x00\x00\x23\x23gdf_sum_squared_generic',0,b'\x00\x00\x10\x23gdf_tan_f32',0,b'\x00\x00\x10\x23gdf_tan_f64',0,b'\x00\x00\x10\x23gdf_tan_generic',0,b'\x00\x00\x14\x23gdf_validity_and',0),
    _struct_unions = ((b'\x00\x00\x00\x50\x00\x00\x00\x10_OpaqueIpcParser',),(b'\x00\x00\x00\x4C\x00\x00\x00\x02gdf_column_',b'\x00\x00\x25\x11data',b'\x00\x00\x2B\x11valid',b'\x00\x00\x09\x11size',b'\x00\x00\x2D\x11dtype')),
    _enums = (b'\x00\x00\x00\x2D\x00\x00\x00\x16$gdf_dtype\x00GDF_invalid,GDF_INT8,GDF_INT16,GDF_INT32,GDF_INT64,GDF_FLOAT32,GDF_FLOAT64',b'\x00\x00\x00\x01\x00\x00\x00\x16$gdf_error\x00GDF_SUCCESS,GDF_CUDA_ERROR,GDF_UNSUPPORTED_DTYPE,GDF_COLUMN_SIZE_MISMATCH,GDF_VALIDITY_MISSING'),
    _typenames = (b'\x00\x00\x00\x4Cgdf_column',b'\x00\x00\x00\x2Dgdf_dtype',b'\x00\x00\x00\x01gdf_error',b'\x00\x00\x00\x09gdf_index_type',b'\x00\x00\x00\x09gdf_size_type',b'\x00\x00\x00\x52gdf_valid_type',b'\x00\x00\x00\x50ipc_parser_type'),
)
