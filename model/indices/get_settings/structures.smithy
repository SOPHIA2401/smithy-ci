// SPDX-License-Identifier: Apache-2.0
// 
//  The OpenSearch Contributors require contributions made to
//  this file be licensed under the Apache-2.0 license or a
//  compatible open source license.

namespace OpenSearch

structure GetSettingsIndexInput {
    
    @httpLabel
    @required
    index: IndexName,
   
    // GetSettingsIndexInput CommonParameters START
    @httpQuery("allow_no_indices")
    allow_no_indices: Boolean,

    @httpQuery("expand_wildcards")
    expand_wildcards: ExpandWildcards,

    @httpQuery("flat_settings")
    flat_settings: Boolean,

    @httpQuery("include_defaults")
    include_defaults: String,

    @httpQuery("ignore_unavailable")
    ignore_unavailable: Boolean,

    @httpQuery("local")
    local: Boolean,

    @httpQuery("master_timeout")
    master_timeout: Time,
    
    // GetSettingsIndexInput CommonParameters END

}

structure GetSettingsIndexOutput {

    @httpPayload
    content: Document

}

structure GetSettingsIndexSettingInput {

    @httpLabel
    @required
    index: IndexName,

    @httpLabel
    @required
    setting: String,
   

    // GetSettingsIndexInput CommonParameters START
    @httpQuery("allow_no_indices")
    allow_no_indices: Boolean,

    @httpQuery("expand_wildcards")
    expand_wildcards: ExpandWildcards,

    @httpQuery("flat_settings")
    flat_settings: Boolean,

    @httpQuery("include_defaults")
    include_defaults: String,

    @httpQuery("ignore_unavailable")
    ignore_unavailable: Boolean,

    @httpQuery("local")
    local: Boolean,

    @httpQuery("master_timeout")
    master_timeout: Time,
    
    // GetSettingsIndexInput CommonParameters END

}

structure GetSettingsIndexSettingOutput {

    @httpPayload
    content: Document
    
}

apply GetSettingsIndex @examples([
    {
        title: "Examples for Get settings Index Operation.",
        input: {
            index: "books"
        },
    }
])

apply GetSettingsIndexSetting @examples([
    {
        title: "Examples for Get settings Index-setting Operation.",
        input: {
            index: "books",
            setting: "index"
        }
    }
])


// structure GetSettingsIndexInput {
    
//     @httpLabel
//     @required
//     index: IndexName,
   
//     // GetSettingsIndexInput CommonParameters START
//     @httpQuery("refresh")
//     refresh: Boolean,

//     @httpQuery("timeout")
//     timeout: Time,

//     @httpQuery("wait_for_active_shards")
//     wait_for_active_shards: String,

//     @httpQuery("wait_for_completion")
//     wait_for_completion: Boolean,

//     @httpQuery("requests_per_second")
//     requests_per_second: Integer,

//     @httpQuery("require_alias")
//     require_alias: Boolean,

//     @httpQuery("scroll")
//     scroll: Time,

//     @httpQuery("slices")
//     slices: Integer,

//     @httpQuery("max_docs")
//     max_docs: Integer,
    
//     // GetSettingsIndexInput CommonParameters END

// }